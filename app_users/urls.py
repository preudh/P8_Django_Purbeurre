"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path
from app_users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
