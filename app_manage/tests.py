from django.test import TestCase
from unittest.mock import patch  # import of patch decorator from unittest module
from django.urls import reverse
from app_data_off.models import Category, Product, UserProduct
from django.contrib.auth.models import User


# Create your tests here.

# Mention Legal page
class MentionLegalPageTestCase(TestCase):

    # test the mention legal page return a 200
    def test_mention_page(self):
        response=self.client.get(reverse('termes'))
        self.assertEqual(response.status_code, 200)


# Search Page
class SearchPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.category_mushrooms=Category.objects.create(name='mushrooms')
        self.magic_food=Product.objects.create(name='magic food', category=self.category_mushrooms, nutrition_grade='a')
        self.epic_food=Product.objects.create(name='epic food', category=self.category_mushrooms, nutrition_grade='a')

    # test return if the search is valid
    def test_search_page_returns_200_if_food_found(self):
        query=self.epic_food.name
        response=self.client.get(reverse('search'), {'q': query})
        self.assertEqual(response.status_code, 200)

    # test return 404 if the search is not valid
    def test_search_page_returns_404_if_not_food_found(self):
        query='faux_nom_qui_ne_sera_jamais_trouvé'
        response=self.client.get(reverse('search'), {'q': query})
        self.assertEqual(response.status_code, 404)

    # test pagination is active
    def test_search_page_returns_true_pagination_number(self):
        query=self.epic_food.name
        response=self.client.get(reverse('search'), {'q': query})
        self.assertEqual(response.context['paginate'], True)


# Detail Page
class DetailPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.category_mushrooms=Category.objects.create(name='mushrooms')
        self.magic_food=Product.objects.create(name='magic food', category=self.category_mushrooms)

    # test that detail page returns a 200 if the item exists
    def test_details_page_returns_200(self):
        response=self.client.get(reverse('detail', args=(self.magic_food.id,)))
        self.assertEqual(response.status_code, 200)

    # # test that detail page returns a 404 if the item does not exist
    def test_details_page_returns_404(self):
        fake_id=self.magic_food.id + 1
        response=self.client.get(reverse('detail', args=(fake_id,)))
        self.assertEqual(response.status_code, 404)


# favorite page
class FavoritePageTestCase(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='Zaraki ', email='zaraki.kempachi@bleach.soul')
        self.user.set_password('zarakipassword')
        self.user.save()

    # test favorite page redirect to login not logged users
    def test_favorite_page_redirect_to_login_not_logged_users(self):
        response=self.client.get(reverse('save'))
        self.assertRedirects(response, '/index/')

    # test favorite page return 200 for logged users
    def test_fav_page_return_200(self):
        self.client.force_login(self.user)
        response=self.client.get(reverse('save'))
        self.assertEqual(response.status_code, 200)


# Backup UserProducts
class BackupPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user=User.objects.create(username='Gin ', email='ichimaru.gin@bleach.soul')
        self.user.set_password('ginpassword')
        self.user.save()
        Category.objects.create(name='mushrooms')
        self.category_mushrooms=Category.objects.get(name='mushrooms')
        Product.objects.create(id='1', name='magic food', category=self.category_mushrooms)
        self.magic_food=Product.objects.get(name='magic food')

    # test to add a new backup if user logged
    def test_new_backup_logged_user(self):
        food_id=self.magic_food.id
        old_backup=Product.objects.filter(backup__user_id=self.user).count()
        self.client.force_login(self.user)
        self.client.get(reverse('save', args=(food_id,)))
        new_backup=Product.objects.filter(backup__user_id=self.user).count()
        self.assertEqual(new_backup, old_backup + 1)

    # test no add a food already on backup
    def test_no_add_food_already_on_backup_(self):
        food=Product.objects.filter(name=self.magic_food.name)
        backup=UserProduct.objects.create(user_id=self.user.id)
        backup.food.set(food)
        old_backup=Product.objects.filter(backup__user_id=self.user).count()
        self.client.force_login(self.user)
        self.client.get(reverse('save', args=(self.magic_food.id,)))
        new_backup=Product.objects.filter(backup__user_id=self.user).count()
        self.assertEqual(new_backup, old_backup)

    # test to add a new backup if user not logged is redirected to login
    def test_new_backup_user_not_logged(self):
        food_id=self.magic_food.id
        response=self.client.get(reverse('save', args=(food_id,)))
        self.assertRedirects(response, '/index/')

    # test if a backup belongs to a contact
    def test_a_backup_belongs_to_contact(self):
        food_id=self.magic_food.id
        self.client.force_login(self.user)
        self.client.get(reverse('save', args=(food_id,)))
        backup=UserProduct.objects.first()
        self.assertEqual(self.user.username, backup.user.username)

    # test that a backup belongs to a food
    def test_a_backup_belongs_to_food(self):
        food_id=self.magic_food.id
        self.client.force_login(self.user)
        self.client.get(reverse('save', args=(food_id,)))
        backup=Product.objects.get(backup__user_id=self.user.id)
        self.assertEqual(food_id, backup.id)
