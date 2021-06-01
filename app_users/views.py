# Create your views here.

from app_users.forms import LoginForm, RegisterForm
from django.shortcuts import render


def login(request):
    # create LoginForm() class instance
    loginform = LoginForm()
    return render(request, 'login.html', {'loginform': loginform})


def register(request):
    register = RegisterForm()
    return render(request, 'register.html', {'register': register})
