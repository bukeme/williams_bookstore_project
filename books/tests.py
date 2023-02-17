from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Permission
from books.models import Book, Review
from users.models import CustomUser as User

# Create your tests here.

class BookTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Bassey',
            email='bassey@company.com',
            password='password'
        )
        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title = 'Django',
            author = 'Ukeme',
            price = '39.00'
        )

        self.reviews = Review.objects.create(
            book=self.book,
            author=self.user,
            review = 'Great Book'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Django')
        self.assertEqual(f'{self.book.author}', 'Ukeme')
        self.assertEqual(f'{self.book.price}', '39.00')

    def test_book_list_view_for_logged_in_users(self):
        self.client.login(email='bassey@company.com', password='password')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login'))
        )
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login'))
        )
        self.assertContains(response, 'Log In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='bassey@company.com', password='password')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')
        self.assertTemplateUsed(response, 'books/book_detail.html')