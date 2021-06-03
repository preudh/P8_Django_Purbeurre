"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms
from django.contrib.auth.models import User  # use data base


# create login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data('username')
        password = cleaned_data("password")

        # check that the two fields are correct
        if username and password:
            result = User.objects.filter(username=username, password=password) # filter uniquement sur username> to to
            if len(result) != 1:
                raise forms.ValidationError('username ou mot de pas erroné')

        return cleaned_data


# create account
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)
    # Passwordfield does not exist so that one must use it in widget
    password = forms.CharField(widget=forms.PasswordInput)

