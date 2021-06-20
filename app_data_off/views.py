""" Script to get data from OpenFoodFacts API and record in DB"""
# Create your views here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
from django.db.utils import DataError, IntegrityError
from openfoodfacts import openfoodfacts

# import personal module
from app_data_off.models import Category, Product


def drop_everythings():
    """ Reinitialisation database"""
    Category.objects.all().delete()
    Product.objects.all().delete()


def get_product_off():
    """get 5 categories from fr.OFF database , categories number is limited voluntarily because heroku limits the number
    of row up to 10000 """
    list_categories = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner', 'Biscuits', 'Vins']
    count_product = 1

    for category in list_categories:
        Category.objects.create(name=category)

        for x in category:
            for product in openfoodfacts.products.get_all_by_category(x):
                try:
                    name = product.get("product_name", None)
                    brand = product.get("brands", None)
                    nutrition_grade = product.get("nutrition_grades", None)
                    url = product.get("url", None)
                    image_front_url = product.get('image_front_url', None)
                    image_nutrition_small_url = product.get("image_nutrition_small_url", None)

                    # create and save an object in a single step, use the create() method.
                    while count_product < 10:
                        Product.objects.create(name=name, brand=brand,
                                               nutrition_grade=nutrition_grade,
                                               url=url, image_front_url=image_front_url,
                                               image_nutrition_small_url=image_nutrition_small_url)
                        pprint(Product.name)
                        count_product += 1

                except KeyError:
                    pass

                except DataError:
                    pass

                except IntegrityError:
                    pass
