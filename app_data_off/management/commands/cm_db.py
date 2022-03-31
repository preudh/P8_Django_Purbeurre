""" Script to register data from OpenFoodFacts in the database """

from django.core.management.base import BaseCommand
from django_command_debug.management.base import DebugMixin
from app_data_off.views import drop_everythings, get_product_off

import psycopg2  # Psycopg – PostgreSQL database adapter for Python¶


class Command(DebugMixin, BaseCommand):
    help = 'create and load the database'

    def handle(self, *args, **options):
        self.debug('message')
        conn = None

        try:
            # !!!to use for local database
            # function connect to the existing database, a new connection instance
            # conn = psycopg2.connect(user="postgres",
            #                         password="postgre",
            #                         host="localhost",
            #                         port="5432",
            #                         database="purbeurre"
            #                         )

            # !!!to use only for heroku database according to the env variable given by heroku
            conn = psycopg2.connect(user = "wwhgcmaufvmdym",
                                    password = "dd13375f6d9d34aacd905d3aed15ebdf8cee5c90f8bca4833b507cc39b7d228a",
                                    host = "ec2-54-155-5-151.eu-west-1.compute.amazonaws.com",
                                    port = "5432",
                                    database = "dd2ii9dfa8b5jh"
                                    )

            # create a cursor to perform database operations
            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            print(conn.get_dsn_parameters(), "\n")
            # Execute a query, Print PostgreSQL version, Query the database and obtain data as Python objects
            cursor.execute("SELECT version();")
            # display the PostgreSQL database server version
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
            drop_everythings()
            print("Reinitialisation of purbeurre database")
            get_product_off()
            print("get products from the n categories OFF database")
            # Make the changes to the database persistent
            conn.commit()
            # Close communication with the database
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
