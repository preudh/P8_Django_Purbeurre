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
    """ category model for product"""

    name = models.CharField(max_length=150)

    def __str__(self):  # for debug
        return self.name


class Product(models.Model):
    """ Product model"""

    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    store = models.CharField(max_length=150)
    nutrition_grade = models.CharField(max_length=1)
    url = models.URLField(max_length=150)
    image_front_url = models.URLField()
    image_nutrition_small_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # delete all the category model instances that

    # depend on the product model instance you deleted

    def __str__(self):
        return self.name


class UserProduct(models.Model):
    """ table between Product and User. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
