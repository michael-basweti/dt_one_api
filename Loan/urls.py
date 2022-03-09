from django.urls import path, include
from .import views

urlpatterns = [
    path('request', views.LoansView.as_view(), name='request'),
    path('approve', views.ApproveView.as_view(), name='approve'),
    path('deny', views.DenyLoan.as_view(), name='deny'),
    path('makepayments', views.CreatePayment.as_view(), name='makepayments'),
    path('payavenues', views.GetPayAvenues.as_view(), name='payavenues'),
    path('unprocessed', views.GetUnProcessedLoans.as_view(), name='unprocessed'),
    path('oneunprocessed/<loanid>', views.GetOneUnProcessedLoans.as_view(), name='oneunprocessed'),
    path('userloans', views.GetUserLoans.as_view(), name='userloans'),
    path('loansdue/<startdate>/<enddate>', views.GetLoansDue.as_view(), name='loansdue'),
]