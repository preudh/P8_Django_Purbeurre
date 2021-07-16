# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as django_logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib import messages
# AuthenticationForm is the pre-built Django form logging in a user
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
# personal import
from .forms import NewUserForm


def register_request(request):
    # checks to see if the form is being posted
    if request.method == "POST":
        form = NewUserForm(request.POST)
        # checks to see if the form is valid
        if form.is_valid():
            # If both are true, then the form information is saved under a user
            user = form.save()
            # the user is logged in
            login(request, user)
            #  the user is redirected to the homepage showing a success message.
            messages.success(request, "Registration successful.")  # message ne sert à rien avec crispy
            return redirect('/index/')
        # if the form is not valid, an error message is shown
        messages.error(request, "Unsuccessful registration. Invalid information.")  # meassage ne sert a rien avec crysp
    # if the request is not a POST, then return the blank form in the register HTML template
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # authenticate function is used to verify user credentials (username and password)
            # and return the correct User object stored in the backend.
            user = authenticate(username=username, password=password)
            # If the backend authenticated the credentials, the function will run Django login() to log in to the
            # authenticated user
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")  # ne sert à rien
                # return redirect("main page")
                return redirect('/index/')  # a revoir car doit rediriger vers page principale
            # if the user is not authenticated, it returns a message error
            else:
                messages.error(request, "Invalid username or password.")  # ne sert à rien
        # if the form is not valid, then it returns a similar error message
        else:
            messages.error(request, "Invalid username or password.")  # ne sert à rien
    #  if the request is not a POST, then return the blank form in the login HTML template
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout(request):
    """The logout view, handling logout requests
    :param request: provided by Django
    """
    django_logout(request)
    return redirect(reverse("index"))  # return ver url index after action

