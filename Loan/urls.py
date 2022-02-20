from django.urls import path, include
from .import views

urlpatterns = [
    path('request', views.LoansView.as_view(), name='request'),
]