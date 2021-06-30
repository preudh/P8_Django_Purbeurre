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
    """get 7 categories from fr.OFF database , categories number is limited voluntarily because heroku limits the number
    of row up to 10000, max 1000 product by category """
    list_categories = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']

    for category in list_categories:  # start of outer loop
        cat_id = Category.objects.create(name=category)
        pprint(Category.name)
        count_product = 1  # initialization of the counter of the inner loop while
        while count_product < 10:  # enter 1000 when the loop is working, start of the inner while loop
            for product in openfoodfacts.products.get_all_by_category(category):  # start of inner loop for
                try:
                    name = product.get("product_name", None)
                    brand = product.get("brands", None)
                    nutrition_grade = product.get("nutrition_grades", None)
                    url = product.get("url", None)
                    image_front_url = product.get('image_front_url', None)
                    image_nutrition_small_url = product.get("image_nutrition_small_url", None)
                    store = product.get("stores", None)
                    # create and save an object in a single step, use the create() method.
                    # while count_product < 10, to expand up to 50-100 for production purposes:
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
                pprint(Product.name)

            count_product += 1  # internal loop counter increment

