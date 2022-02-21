from django.urls import path, include
from .import views

urlpatterns = [
    path('request', views.LoansView.as_view(), name='request'),
    path('approve', views.ApproveView.as_view(), name='approve'),
    path('deny', views.DenyLoan.as_view(), name='deny'),
    path('payavenues', views.GetPayAvenues.as_view(), name='payavenues'),
]