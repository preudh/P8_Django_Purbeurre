"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path, include
from app_users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout, name='logout'),
]
