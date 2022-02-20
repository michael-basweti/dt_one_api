from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Loans, Payavenue, Payments, Paymenttype
from .serializers import LoansSerializer, PaymentsSerializer
from rest_framework import generics, permissions, status
from utils.register_email import loan_acknowledgement


class LoansView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = UserSerializer

    # def get(self, request):
    #     users = User.objects.filter(deleted=False)
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = LoansSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(requestedby=request.user)
            emailUser = request.user.email
            # aws_email_send(emailUser, password)
            # gmail_send_email(emailUser, password)
            loan_acknowledgement(emailUser)
            data = {
                "data": serializer.data,
                "message": "Loan successfully submitted"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response((serializer.errors), status=status.HTTP_400_BAD_REQUEST)
