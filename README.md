## OC Project 8: set up ap web application for a restaurant to propose better product


### Description

This project is part of the OC Python developer course.

The Pur Beurre start-up, for which you have already worked decides to set up a web application that allows 
customers to find healthy alternatives (better nutriscore) :

* The [OpenFoodFacts](https://fr.openfoodfacts.org/) Data
* Use of the web framework Django
* Test driven development : unittest and functional test with selenium
* Responsive interface with bootstrap CSS framework

### Functionalities 

* Search field from the home page
* The search must not be using AJAX
* The customer can create a user account and login/logout
* The customer can save searchs and delete them
* the customer can see the details of the products
* Responsive interface


### Utilisation and softwares needeed
*in your local desktop
* Set up virtual environment in your IDE (e.g. Pycharm or VSC)
* Use python 3.11.4 as a base interpreter for heroku 
* create your database (e.g. with pgadmin 4)
* settings of the database in settings.py
* make migrations 
```
python manage.py makemigrations
python manage.py migrate
```
*load the database with categories and products according to the categories listed in the constante.py file
which is in the directory /app_data_off/management/commands/constante.py

to do that use the command in your terminal
```
python manage.py cm_db
```

* run the local server in your IDE


* with heroku

You can view the application here: https://p8-django-purbeurre-37bbf40223b7.herokuapp.com/

You can search alternatives for these categories (e.g.):

* Aides culinaires
* Chocolats
* Epicerie
* Poissons
* Rillettes de poissons
* Sardines à l'huile
* Viandes


