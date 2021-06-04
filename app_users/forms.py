"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class LoginForm(forms.Form):
#     # create login form
#     username = forms.CharField(label="username", max_length=50)
#     password = forms.CharField(label="password", widget=forms.PasswordInput)
#
#
# class CustomUserCreationForm(forms.Form):
#     username = forms.CharField(label='Enter Username', min_length=4, max_length=10)
#     email = forms.EmailField(label='Enter email')
#     password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise ValidationError("Username already exists")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         r = User.objects.filter(email=email)
#         if r.count():
#             raise ValidationError("Email already exists")
#         return email
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")
#
#         return password2
#
#     def save(self, commit=True):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             self.cleaned_data['email'],
#             self.cleaned_data['password1']
#         )
#         return user

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
