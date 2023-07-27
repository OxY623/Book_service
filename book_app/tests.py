from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your tests here.
class AuthorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')

    def test_get_author_list(self):
        url = reverse('author-list')
        response = self.client.get(url)
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_author(self):
        url = reverse('author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)
        self.assertEqual(Author.objects.get(pk=response.data['id']).name, 'New Author')


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')
        self.book1 = Book.objects.create(title='Book 1')
        self.book2 = Book.objects.create(title='Book 2')
        self.book1.authors.add(self.author1, self.author2)
        self.book2.authors.add(self.author2)

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'authors': [self.author1.id, self.author2.id]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertTrue(self.author1 in response.data['authors'])
        self.assertTrue(self.author2 in response.data['authors'])
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

# Create your tests here.
