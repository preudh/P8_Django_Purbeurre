# Create your models here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" Models declaration """

from django.db import models
# Using the Django authentication system
# User objects represent the people who interact with your site and are used to activate features such as restricting
# access, registering user profiles, associating content with its creator, etc.
from django.contrib.auth.models import User


class Category(models.Model):
    """ category model"""

    name = models.CharField(max_length=150)

    def __str__(self):  # pour debug
        return self.name


class Product(models.Model):
    """ Product model"""

    name = models.CharField(max_length=150)
    brands = models.CharField(max_length=150)
    stores = models.CharField(max_length=150)
    nutriscore_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=150)
    image_front_url = models.CharField(max_length=150)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)  # delete all the category model instances that
    # depend on the product model instance you deleted

    def __str__(self):
        return self.name


class UserSustitut(models.Model):
    """ table between Substitut and User. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
