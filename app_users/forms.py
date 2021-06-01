"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms


# create login form
class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


# create account
class RegisterForm(forms.Form):
    name = forms.CharField(
        label="Name",
        # used the attribute form control to take advantage of bootstrap sizing components
        widget=forms.TextInput(attrs={'class': 'form-control'}), )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        # the field is required
        required=True)
    # Passwordfield does not exist so that one must use it in widget
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)



