from django.urls import path, include
from .import views

urlpatterns = [
    path('register', views.UserCreateView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('update_password',views.UpdateUserPassword.as_view(), name='update_password'),
]