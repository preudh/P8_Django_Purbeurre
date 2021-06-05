"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # only once empty
    path('', views.index, name='index'),
    path('termes/', views.termes, name='termes'),
    path('base/', views.base, name='base'),
]
