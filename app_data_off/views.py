# Create your views here.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import random
from django.db.utils import DataError, IntegrityError
# import personal module
from app_data_off.models import Category, Product


def drop_everythings():
    """ Reinitialisation of purbeurre database"""
    Category.objects.all().delete()
    Product.objects.all().delete()


def get_category_off():
    """get N randomized categories from fr.OFF database"""
    # list_categories = []
    cat = requests.get('https://fr.openfoodfacts.org/categories?json=true')
    cat_data = cat.json()
    tags_list = cat_data['tags']
    print(len(tags_list))
    # 5 random categories used for the tests
    list_categories = random.sample(tags_list, k=5)
    for category in list_categories:
        Category.objects.create(name=category)


def get_product_data_off(list_categories):
    """method to get products from OFF database"""
    list_products = []
    for x in list_categories:
        """get products' data from openfoodfacts api with string as paramaters"""
        parameters = {
            'action': 'process',
            'json': 1,
            'countries': 'France',
            'page_size': 300,  # 24 products per page * 300 = 7500 ok with heroku storage
            'page': 1,
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': x
        }
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
                         params=parameters)  # passing parameters in URL
        print(r.url)
        data = r.json()  # r. from requests module decodes json file
        products = data['products']  # access dictionary items by referring to its key name, products ordered by id
        list_products.append(products)

        for product in list_products:
            try:
                name = product["product_name"]
                brand = product["brands"]
                nutrition_grade = product["nutrition_grades"]
                url = product["url"]
                image_front_url = product['image_front_url']
                image_nutrition_small_url = product["image_nutrition_small_url"]
                # create and save an object in a single step, use the create() method.
                Product.objects.create(name=name, brand=brand,
                                       nutrition_grade=nutrition_grade,
                                       url=url, image_front_url=image_front_url,
                                       image_nutrition_small_url=image_nutrition_small_url)

            except KeyError:
                pass

            except DataError:
                pass

            except IntegrityError:
                pass
