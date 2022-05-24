from django.urls import path, include
from django.conf import settings
from django.shortcuts import render
from . import views

urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('home/', views.home, name= 'home'),

]

