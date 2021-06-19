""" Script to register data from OpenFoodFacts in the database """

from django.core.management.base import BaseCommand
from django_command_debug.management.base import DebugMixin
from app_data_off.views import drop_everythings, get_category_off, get_product_data_off

import psycopg2  # Psycopg – PostgreSQL database adapter for Python¶


class Command(DebugMixin, BaseCommand):
    help = 'create and load the database'

    def handle(self, *args, **options):
        self.debug('message')
        conn = None

        try:
            # function connect to the existing database, a new connection instance
            conn = psycopg2.connect(user="postgres",
                                    password="postrgre",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="purbeurre")

            # create a cursor to perform database operations
            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            print(conn.get_dsn_parameters(), "\n")
            # Execute a query, Print PostgreSQL version, Query the database and obtain data as Python objects
            cursor.execute("SELECT version();")
            # display the PostgreSQL database server version
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

        drop_everythings()
        print("Reinitialisation of purbeurre database")
        get_category_off()
        print("get 5 randomized categories from fr.OFF database")
        # get_product_data_off(get_category_off())
        # for test purposes if no request from OFF when user input his search
        list_categories = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner', 'Biscuits', 'Vins']
        category = list_categories
        # get_product_data_off(category=category)
        get_product_data_off(list_categories)
        print("get products from the 5 categories OFF database")
        # Make the changes to the database persistent
        conn.commit()
        # Close communication with the database
        # cursor.close()
        # conn.close()
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection closed.')