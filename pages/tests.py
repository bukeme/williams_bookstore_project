from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from pages.views import AboutPageView, HomePageView

# Create your tests here.

class PagesTests(SimpleTestCase):
    def test_home_page_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_page_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutTestPage(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)