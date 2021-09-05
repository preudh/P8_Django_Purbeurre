"""P8_Django_Purbeurre URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # only once empty
    path('', views.index, name='index'),
    path('termes/', views.termes, name='termes'),
    path('base/', views.base, name='base'),
    path('index/', views.index, name="index"),
    path('substitute/', views.substitute, name='substitute'),
    # path('substitute/save_substitut/', views.save_substitut, name='save_substitut'),
#     path('product/<pk>/', views.Detail.as_view(), views.Detail, name='details'),
#     path('substitute/', views.Substitute, name='substitute'),
]
