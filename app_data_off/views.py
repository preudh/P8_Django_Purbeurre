""" Script to get data from OpenFoodFacts API and record in DB"""
# Create your views here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import django
from pprint import pprint
from django.db.utils import DataError, IntegrityError
from openfoodfacts import openfoodfacts
from django.db import models
from django.db.models.query_utils import DeferredAttribute
# import personal module
from app_data_off.models import Category, Product


def drop_everythings():
    """ Reinitialisation database"""
    Category.objects.all().delete()
    Product.objects.all().delete()


def get_product_off():
    """get 7 categories from fr.OFF database , categories number is limited voluntarily because heroku limits the number
    of row up to 10000, max 1000 product by category """
    list_categories = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']

    for category in list_categories:  # début de la boucle externe
        cat_id = Category.objects.create(name=category)
        # cat_id = cat_id.id
        pprint(Category.name)
        # cat_id = Category.objects.get(name=category)
        # cat_id = cat_id[0].id
        count_product = 1  # initialisation du compteur de la boucle interne while  n°1
        while count_product < 10:  # enter 1000 quand la boucle fonctionne, début de la boucle interne while  n°1
            # print(product['product_name'])
            for product in openfoodfacts.products.get_all_by_category(category):  # début de la boucle interne for n°2
                try:
                    name = product.get("product_name", None)
                    brand = product.get("brands", None)
                    nutrition_grade = product.get("nutrition_grades", None)
                    url = product.get("url", None)
                    image_front_url = product.get('image_front_url', None)
                    image_nutrition_small_url = product.get("image_nutrition_small_url", None)
                    store = product.get("stores", None)
                    # create and save an object in a single step, use the create() method.
                    # while count_product < 10:
                    Product.objects.create(name=name, brand=brand,
                                           store=store,
                                           nutrition_grade=nutrition_grade,
                                           url=url, image_front_url=image_front_url,
                                           image_nutrition_small_url=image_nutrition_small_url,
                                           category=cat_id)

                except KeyError:
                    pass

                except DataError:
                    pass

                except IntegrityError:
                    pass
                pprint(Product.name)  # fin de la boucle interne for  n°2

            count_product += 1  # incrémentation du compteur de la boucle interne while n°1

        # Category.objects.create(name=category)
        # pprint(Category.name)  # fin de la boucle externe for
