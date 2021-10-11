"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('termes/', views.termes, name='termes'),
    path('base/', views.base, name='base'),
    path('index/', views.index, name="index"),
    path('search/', views.search, name='search'),
]
