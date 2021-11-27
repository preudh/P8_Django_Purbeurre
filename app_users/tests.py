from django.test import TestCase
from django.contrib.auth.models import User
from P8_Django_Purbeurre.app_users.views import register_request

# Create your tests here.

# Register Page
from django.urls import reverse


class RegisterPageTestCase(TestCase):

    # test register a new user
    def test_new_user_registered(self): # garder le nom de la methode
        old_users=User.objects.count() # ne pas faire
        password='Testpassword'
        user=User.objects.create(username='Regis', email='register@test.com')
        user.set_password(password)
        user.save()
        username=user.username
        email=user.email
        password=user.password
        self.client.post(reverse('register_request'), {
            'name': username,
            'email': email,
            'password': password
        })
        new_users=User.objects.count()
        self.assertEqual(new_users, old_users + 1)


# Login Page
class LoginPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user=User.objects.create(username='Saitama', email='saitama@one.punch')
        self.user.set_password('testpassword')
        self.user.save()

    # test if login page authenticated user
    def test_login(self):
        response=self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': 'testpassword'
        }, follow=True)
        self.client.login(username=self.user.username, password=self.user.password)
        self.assertTrue(response.context['user'].is_authenticated)

    # test if login page return Anonymous with fake user
    def test_login_fake_user(self):
        response=self.client.post(reverse('login'), {
            'username': 'Fake_user',
            'password': 'fakepassword'
        }, follow=True)
        self.client.login(username='Fake_user', password='fakepassword')
        self.assertTrue(response.context['user'].is_anonymous)


# Logout Page
class LogoutPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user=User.objects.create(username='Kisuke ', email='urahara.kisuke@bleach.soul')
        self.user.set_password('kisukepassword')
        self.user.save()

    # test if logout page return anonyme user
    def test_logout(self):
        self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': 'kisukepassword'
        }, follow=True)
        self.client.login(username=self.user.username, password=self.user.password)
        response=self.client.post(reverse('logout'), follow=True)
        self.client.logout()
        self.assertTrue(response.context['user'].is_anonymous)
