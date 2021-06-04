# Create your views here.
# user object authentication system
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# allows to temporarily store messages in one request and retrieve them for display in a subsequent request
# from django.contrib import messages
# from django.shortcuts import render, redirect
# # Use authenticate() to verify username and password for the default case
# from django.contrib.auth import authenticate, login
# # from app_users.forms import LoginForm, CustomUserCreationForm
# from app_users.forms import NewUserForm


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 # redirect to the success page home.html
#                 return render(request, 'home.html')
#             else:
#                 # Return an 'invalid login' error message.
#                 messages.error(request, "Identifiants invalides")
#                 return render(request, 'login.html', {'form': form})
#     return render(request, 'login.html')
#
#
# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
