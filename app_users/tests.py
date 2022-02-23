from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class CustomUserTests(TestCase):
    """ we do not need to test all log in and log out features since those are built into Django and have already tests
    except test for several users that must not have the same email"""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData() is called once at the start of the test run for class-level tuning. You can use it to
        create objects that are not meant to be modified or changed in test methods. """

        cls.user=get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret",
        )

    def setUp(self):
        url=reverse('register')
        self.response=self.client.get(url)

    # ok
    def test_login_request_page_returns_200(self):
        """ Login page returns 200 """
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # ok
    def test_bad_url_returns_404(self):
        """ Bad URL returns 404 """
        no_response=self.client.get('badurl')
        self.assertEqual(no_response.status_code, 404)

    # ok
    def test_good_login_returns_true(self):
        """ Test login with good credentials """
        login=self.client.login(username="testuser", email="test@email.com", password="secret")
        self.assertTrue(login)

    # ok
    def test_register_request(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)

    def test_not_possible_create_users_with_same_email():
        user_1=User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123',
        )
        user_2=User.objects.create_user(
            username='bob',
            email='will@email.com',
            password='testpass124',
        )
        # error message in case if test case got failed
        message="email value and second value are equal !"
        # make sure we can't create a second user with the same email.
        self.assertEqual(user_1.email, user_2.email, message)
        with user_1.email == user_2.email:
            self.assertTrue(False)

    # ok
    def test_register_page_status_name(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    # ok
    def test_register_url_name(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    # TODO
    def test_register_correct_template(self):
        self.client.login(username="testuser", email="test@email.com", password="secret")
        response=self.client.get(reverse("register"))
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, "testuser")
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_logout_page_returns_200(self):
        """ Logout page returns 200 """
        response=self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
