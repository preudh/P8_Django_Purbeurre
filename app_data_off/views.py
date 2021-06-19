""" Script to get data from OpenFoodFacts API"""
# Create your views here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
import requests
from django.db.utils import DataError, IntegrityError
# import personal module
from openfoodfacts import openfoodfacts
from app_data_off.models import Category, Product


def drop_everythings():
    """ Reinitialisation of purbeurre database"""
    Category.objects.all().delete()
    Product.objects.all().delete()


def get_category_off():
    """get 5 categories from fr.OFF databas"""
    list_categories = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner', 'Biscuits', 'Vins']

    for category in list_categories:
        try:
            Category.objects.create(name=category)

        except KeyError:
            pass
        except UnicodeEncodeError:
            pass


def get_product_data_off(list_categories):
    """method to get products from OFF API and recording them in DB"""

    for product in openfoodfacts.products.get_all_by_category(list_categories):
        print(product['product_name'])

        name = product.get["product_name", None]
        brand = product.get["brands", None]
        nutrition_grade = product.get["nutrition_grades", None]
        url = product.get["url", None]
        image_front_url = product.get['image_front_url', None]
        image_nutrition_small_url = product.get["image_nutrition_small_url", None]

        # create and save an object in a single step, use the create() method.
        try:
            Product.objects.create(name=name, brand=brand,
                                   nutrition_grade=nutrition_grade,
                                   url=url, image_front_url=image_front_url,
                                   image_nutrition_small_url=image_nutrition_small_url)
            pprint(product)
        except KeyError:
            pass

        except DataError:
            pass

        except IntegrityError:
            pass
