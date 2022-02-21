import random
import string

import jwt
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.models import (
    update_last_login
)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.register_email import gmail_send_email

from .models import (User, Usertypes)
from .serializers import (UserSerializer,UserTypeSerializer)



class UserCreateView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.filter(deleted=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializerUser = UserSerializer(data=request.data, partial=True)
        password = ''.join(random.SystemRandom().choice(
            string.ascii_letters + string.digits) for _ in range(10))

        if serializerUser.is_valid():
            serializerUser.save(password=password)
            emailUser = request.data.get('email')
            # aws_email_send(emailUser, password)
            gmail_send_email(emailUser, password)
            data = {
                "data": serializerUser.data,
                "message": "Account Created Successfully, Kindly check your email for the password"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response((serializerUser.errors), status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        user_info = request.data
        email = user_info.get('email', None)
        password = user_info.get('password', None)
        user = authenticate(email=email, password=password)

        if user:
            activeCheck = User.objects.get(email=email)
            auth_token = jwt.encode(
                {'email': user.email}, settings.JWT_SECRET_KEY)
            serializer_class = UserSerializer(user)
            data = {
                'user': serializer_class.data,
                'token': auth_token
            }
            update_last_login(None, activeCheck)

            return Response(data, status=status.HTTP_200_OK)
        error = {
            'detail': 'Invalid Credentials'
        }

        return Response(error, status=status.HTTP_401_UNAUTHORIZED)


class UpdateUserPassword(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        old_password = request.data.get('old_password')
        password1 = request.data.get('password1')
        password = request.data.get('password')
        user = request.user
        # verify password
        pass_check = user.check_password(old_password)
        if password != password1:
            data = {
                "message": "password update error",
                "real_message": "password1 is not equal to password2"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        if not pass_check:
            data = {
                "message": "password update error",
                "real_message": "old password is not correct"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("ok")
            serializer_class = UserSerializer(
                user, {"password": password}, partial=True)
            if serializer_class.is_valid():
                serializer_class.save()

                # login
                user = authenticate(
                    email=request.user.email, password=password)

                if user:
                    auth_token = jwt.encode(
                        {'email': user.email}, settings.JWT_SECRET_KEY)
                    serializer_class_login = UserSerializer(user)
                    data = {
                        'message': "Password successfully updated",
                        'user': serializer_class_login.data,
                        'token': auth_token
                    }

                    return Response(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'detail': 'Invalid Credentials'
                    }
                    return Response(data, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)