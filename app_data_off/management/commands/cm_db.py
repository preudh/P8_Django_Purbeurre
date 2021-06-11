from django.core.management.base import BaseCommand
from app_data_off.views import drop_everythings, get_category_off, get_product_data_off
import psycopg2.errors


class Command(BaseCommand):
    help = 'create and load the database'

    def handle(self, **options):
        try:
            conn = psycopg2.connect(user="postgres",
                                    password="postrgre",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="purbeurre")

            cursor = conn.cursor()
            # Print PostgreSQL Connection properties
            print(conn.get_dsn_parameters(), "\n")
            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        drop_everythings()
        print("Reinitialisation of purbeurre database")
        get_category_off()
        print("get N randomized categories from fr.OFF database")
        get_product_data_off(get_category_off)
        print("get products from OFF database")
