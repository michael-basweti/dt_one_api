import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from Authentication.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        # print(auth_data)

        if not auth_data:
            return None
        
        prefix,token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])

            user = User.objects.get(email=payload['email'])
            # print(user,token)
            return(user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid, login')
        except jwt.ExpiredSignature as identifier:
            raise exceptions.AuthenticationFailed('Your token is Expired, login')
        return super().authenticate(request)