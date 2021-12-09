"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path
from app_users import views
# from django.contrib import admin
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    # path('admin', admin.site.urls)
]
