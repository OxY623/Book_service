from django.test import TestCase
from .models import Author, Book


class AuthorModelTests(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name='John Doe')
        self.assertEqual(author.name, 'John Doe')
        self.assertEqual(Author.objects.count(), 1)

    def test_author_string_representation(self):
        author = Author.objects.create(name='John Doe')
        self.assertEqual(str(author), 'John Doe')


class BookModelTests(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')
        self.book = Book.objects.create(title='Test Book')

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.authors.count(), 0)

        self.book.authors.add(self.author1)
        self.book.save()

        self.assertEqual(self.book.authors.count(), 1)
        self.assertTrue(self.author1 in self.book.authors.all())

    def test_book_string_representation(self):
        self.assertEqual(str(self.book), 'Test Book')