import self
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import Validator, register_request


class CustomUserTests(TestCase):
    """ we do not need to test all log in and log out features since those are built into Django and have already tests
    except test for several users that must not have the same email"""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData() is called once at the start of the test run for class-level tuning. You can use it to
        create objects that are not meant to be modified or changed in test methods. """
        # Create a user used to test_good_login_returns_true
        cls.user=get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret",
        )
        # Create a user 1
        cls.user_1=User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123',
        )
        # Create a user 2
        cls.user_2=User.objects.create_user(
            username='bob',
            email='will@email.com',
            password='testpass124',
        )

    # ok
    def test_create_user_content(self):
        self.assertEqual(self.user_1.username, 'will')
        self.assertEqual(self.user_1.email, 'will@email.com')
        self.assertTrue(self.user_1.is_active)

    # ok
    def test_register_page_status_code(self):
        response=self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    # ok
    def test_register_page_url_by_name(self):
        response=self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    # ok
    def test_register_correct_template(self):
        response=self.client.get(reverse("register"))
        self.assertTemplateUsed(response, 'register.html')

    # ok
    def test_valid_email_not_exist(self):
        self.assertFalse(Validator.valid_email_exist('toto@gmail.com'))

    # ok
    def test_valid_email_exist(self):
        self.assertTrue(Validator.valid_email_exist('will@email.com'))

    # TODO
    def test_not_possible_create_users_with_same_email(self):
        class MockRegister:
            def __init__(self, dic):
                self.META={"CSRF_COOKIE": "test"}
                self.method='POST'
                self.POST=dic

        dict={"username": "test", "email": 'will@email.com', "password1": "@a123@!Ab", "password2": "@a123@!Ab"}
        mock=MockRegister(dict)
        self.assertRedirects(register_request(mock), 200)

    # ok
    def test_login_request_page_returns_200(self):
        """ Login page returns 200 """
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # ok
    def test_login_page_status_name(self):
        response=self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    # ok
    def test_login_url_name(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    # ok prerequisite is to define def setUpTestData(cls):
    def test_good_login_returns_true(self):
        """ Test login with good credentials """
        login=self.client.login(username="testuser", email="test@email.com", password="secret")
        self.assertTrue(login)

    # ok
    def test_logout_page_returns_200(self):
        """ Logout page returns 200 """
        response=self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
