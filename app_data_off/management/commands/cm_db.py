""" Script to register data from OpenFoodFacts in the database """
from django.core.management.base import BaseCommand
from app_data_off.views import drop_everythings, get_category_off, get_product_data_off
import psycopg2  # Psycopg – PostgreSQL database adapter for Python¶


class Command(BaseCommand):
    help = 'create and load the database'

    def handle(self, **options):
        try:
            # function connect to an existing database, a new connection instance
            conn = psycopg2.connect(user="postgres",
                                    password="postrgre",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="purbeurre")

            # Open a cursor to perform database operations
            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            print(conn.get_dsn_parameters(), "\n")
            # Execute a query, Print PostgreSQL version, Query the database and obtain data as Python objects
            cursor.execute("SELECT version();")
            # Retrieve query results
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        drop_everythings()
        print("Reinitialisation of purbeurre database")
        get_category_off()
        print("get 5 randomized categories from fr.OFF database")
        # get_product_data_off(get_category_off())
        get_product_data_off()
        print("get products from the 5 categories OFF database")

        # Make the changes to the database persistent
        # conn.commit()

        # Close communication with the database
        # cursor.close()
        # conn.close()
