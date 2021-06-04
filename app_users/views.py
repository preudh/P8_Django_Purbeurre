# Create your views here.

from app_users.forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect


def login(request):
    # create LoginForm() class instance
    if len(request.POST) > 0:  # test if form is sent
        # creation of an object LoginForm type to which one pass it POST data of the request HTTP
        login = LoginForm(request.POST)
        if login.is_valid():  # method to validate all form fields
            return redirect('/home')  # if form validated, user is redirected to home page
        else:
            # display again login.html with incorrect fields
            return render(request, 'login.html', {'login': login})
    else:
        # creation of an blank object LoginForm passed to template
        login = LoginForm()
        return render(request, 'login.html', {'login': login})


def register(request):
    # register = RegisterForm()
    # print(request.method)
    # if request.method == 'GET':
    #     register = RegisterForm()
    #     return render(request, 'register.html', {'register': register})
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
