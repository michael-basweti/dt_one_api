from functools import partial
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Loans, Payavenue
from .serializers import LoansSerializer, PaymentsSerializer, PayavenueSerializer
from rest_framework import permissions, status
from utils.register_email import loan_acknowledgement,loan_approval, loan_denied

class LoansView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

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


class ApproveView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        loanid = request.data.get('loanid')
        amountdispatched = request.data.get('amountdispatched')
        approvalcomments = request.data.get('approvalcomments')

        try:
            loan = Loans.objects.get(loanid=loanid)
        except Loans.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dataLoan = {
            "amountdispatched":amountdispatched,
            "approvalcomments":approvalcomments,
            "approved":True
        }

        datapay = {
            "amountpaid":amountdispatched,
            "paymenttype":2,
            "payavenue":loan.payavenue.payavenueid
        }

        loanSerializer = LoansSerializer(loan,data=dataLoan,partial=True)
        payserializer = PaymentsSerializer(data=datapay,partial=True)

        if loanSerializer.is_valid():
            if payserializer.is_valid():
                loanSerializer.save(approvedby=request.user)
                payserializer.save(processedby=request.user)

                emailUser = loan.requestedby.email

                loan_approval(emailUser)

                data = {
                    "message":"Loan Approved"
                }

                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(payserializer.errors, status=status.HTTP_200_OK)
        else:
            return Response(loanSerializer.errors, status=status.HTTP_200_OK)



class DenyLoan(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request):
        loanid = request.data.get('loanid')
        deniedreason = request.data.get('deniedreason')


        data = {
            "deniedreason":deniedreason,
            "denied":True
        }

        try:
            loan = Loans.objects.get(loanid=loanid)
        except Loans.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        loanSerializer = LoansSerializer(loan,data=data,partial=True)

        if loanSerializer.is_valid():
            loanSerializer.save(approvedby=request.user)
            emailUser = loan.requestedby.email
            loan_denied(emailUser)
            data = {
                "message":"Loan denied"
            }

            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response(loanSerializer.errors, status=status.HTTP_200_OK)



# Get Pay Avenues

class GetPayAvenues(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        avenues = Payavenue.objects.all()
        serializer = PayavenueSerializer(avenues, many=True)
        return Response(serializer.data)