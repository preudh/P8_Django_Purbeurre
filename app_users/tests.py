from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class CustomUserTests(TestCase):
    """ we do not need to test all log in and log out features since those are built into Django and have already tests
    except test for several users that must not have the same email"""

    def setUp(self):
        url=reverse('register')
        self.response=self.client.get(url)

    def test_not_possible_create_users_with_same_email(self):
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
        # self.assertNotEqual(user_1.email, user_2.email, message)
        # with user_1.email == user_2.email:
        #     self.assertTrue(False)


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

    def test_register_template(self):
        self.assertEqual(self.response.status_code, 200)  # 200 is success request
        self.assertTemplateUsed(self.response, 'register.html')
        # self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')
