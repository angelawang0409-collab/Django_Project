# Import Django's TestCase class for writing tests and Client for simulating requests
from django.test import TestCase, Client
# Import Django's authentication system to get the User model
from django.contrib.auth import get_user_model
# Import reverse to generate URLs by name
from django.urls import reverse
# Import the Book model to test
from .models import Book


# Test class for testing Book model and views
class BookTest(TestCase):

    # Setup method runs before each test - creates test data
    def setUp(self):
        # Create a test user with credentials for login tests
        self.user = get_user_model().objects.create_user(
            username = 'yash',
            email = 'yashmarmat08@gmail.com',
            password = 'secret',
        )

        # Create a test book with all required fields
        self.book = Book.objects.create(
            title = 'django for beginners',
            author = 'WS Vincent',
            description = 'anything',
            price = '30',
            image_url = 'https://forexample.jpg',
            follow_author = 'https://twitter.com/wsv3000?lang=en',
            book_available = 'True',
        )

    # Test that the book's string representation returns its title
    def test_string_representation(self):
        book = Book(title='new book')
        self.assertEqual(str(book), book.title)

    # Test that all book model fields contain correct data
    def test_book_model_fields_content(self):
        self.assertEqual(f'{self.book.title}', 'django for beginners')
        self.assertEqual(f'{self.book.author}', 'WS Vincent')
        self.assertEqual(f'{self.book.description}', 'anything')
        self.assertEqual(f'{self.book.price}', '30')
        self.assertEqual(f'{self.book.image_url}', 'https://forexample.jpg')
        self.assertEqual(f'{self.book.follow_author}', 'https://twitter.com/wsv3000?lang=en')
        self.assertEqual(f'{self.book.book_available}', 'True')

    # Test book list view is accessible to logged-in users and displays book data
    def test_book_list_view_for_logged_in_user(self):
        self.client.login(username = 'yash', email='yashmarmat08@gmail.com', password='secret')
        request = self.client.get(reverse('list'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'django for beginners')
        self.assertContains(request, '30')

    # Test book list view is accessible to anonymous users (no login required)
    def test_book_list_view_for_anonymous_user(self):
        self.client.logout()
        request = self.client.get(reverse('list'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'django for beginners')
        self.assertContains(request, '30')

    # Test book detail view shows all book information for logged-in users
    def test_book_detail_view_for_logged_in_user(self):
        self.client.login(username = 'yash', email='yashmarmat08@gmail.com', password='secret')
        request = self.client.get(reverse('detail', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'django for beginners')
        self.assertContains(request, 'WS Vincent')
        self.assertContains(request, '30')

    # Test book detail view is accessible to anonymous users
    def test_book_detail_view_for_anonymous_user(self):
        self.client.logout()
        request = self.client.get(reverse('detail', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'django for beginners')
        self.assertContains(request, 'WS Vincent')
        self.assertContains(request, '30')

    # Test checkout view is accessible to logged-in users
    def test_checkout_view_for_logged_in_user(self):
        self.client.login(username = 'yash', email='yashmarmat08@gmail.com', password='secret')
        request = self.client.get(reverse('checkout', args='1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'django for beginners')
        self.assertContains(request, '30')

    # Test checkout view redirects anonymous users to login page
    def test_checkout_view_for_anonymous_user(self):
        self.client.logout()
        request = self.client.get(reverse('checkout', args='1'))
        self.assertEqual(request.status_code, 302)  # 302 = redirect
        self.assertRedirects(request, '/accounts/login/?next=/1/checkout/')

    # Test that available books show "Buy Now" button and not "Out of Stock"
    def test_book_when_available(self):
        request = self.client.get(reverse('detail', args = '1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'Buy Now') 
        self.assertNotContains(request, 'Out of Stock !')

    # Test that out-of-stock books show "Out of Stock" and hide "Buy Now" button
    def test_book_when_out_of_stock(self):
        # Create a second book that's out of stock
        book = Book.objects.create(
            title = 'new book',
            author = 'yash',
            description = 'anything',
            price = '30',
            image_url = 'https://forexample.jpg',
            follow_author = 'https://twitter.com/wsv3000?lang=en',
            book_available = 'False',   # False = out of stock
        )
        request = self.client.get(reverse('detail', args = '2'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'Out of Stock !')
        self.assertNotContains(request, 'Buy Now')