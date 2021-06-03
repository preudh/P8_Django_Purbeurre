# Create your views here.

from app_users.forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect


def login(request):
    # create LoginForm() class instance
    loginform = LoginForm()
    return render(request, 'login.html', {'loginform': loginform})


def register(request):
    # register = RegisterForm()
    if len(request.POST) > 0:
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect('/login')
        else:
            return render(request, 'register.html', {'register': register})
    else:
        register = RegisterForm()
        return render(request, 'register.html', {'register': register})
