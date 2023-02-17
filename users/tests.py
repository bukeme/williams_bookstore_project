from django.test import TestCase
from users.forms import CustomUserCreationForm
from users.models import CustomUser as User
from django.urls import reverse, resolve

from users.views import SignUpView

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email = 'uk@company.com',
            username = 'uk',
            password = 'testing321'
        )
        self.assertEqual(user.email, 'uk@company.com')
        self.assertEqual(user.username, 'uk')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email = 'uk@company.com',
            username = 'uk',
            password = 'testing321'
        )
        self.assertEqual(user.email, 'uk@company.com')
        self.assertEqual(user.username, 'uk')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignUpPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@company.com'
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_page_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Sign Up')
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_form(self):
        user = User.objects.create_user(
            username=self.username,
            email=self.email
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.email)

    