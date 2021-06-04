"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User  # use data base


# create login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # validation of username and password
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data('username')
        password = cleaned_data("password")

        if username and password:
            # search user whose name and password match with database
            result = User.objects.filter(username=username, password=password)  # filter uniquement sur username> to validate
            # check that there is only one result
            if len(result) != 1:
                raise forms.ValidationError('username ou mot de pas erroné')

        return cleaned_data


# create account
class RegisterForm(ModelForm):
    # class to create account
        username = forms.CharField(widget=forms.TextInput)
        email = forms.EmailField(max_length=50, widget=forms.EmailInput)
        # Passwordfield does not exist so that one must use it in widget
        password = forms.CharField(widget=forms.PasswordInput)

