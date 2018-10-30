from django.urls import path
from django.conf.urls import url
from . import views
from django.shortcuts import redirect


app_name = 'User_Login'

urlpatterns = [
    path('', views.Signup, name = 'signup')
]