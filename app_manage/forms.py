"""Declaring a form is very similar to declaring a template. It is also
from a class inheriting from a parent class provided by Django. The attributes also match
to the form fields."""

from django import forms


class SearchForm(forms.Form):
    """ Form to search a product. Display on nav and index page. """
    search = forms.CharField(max_length=50)
