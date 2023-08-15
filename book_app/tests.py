from django.test import TestCase
from .models import Author, Book


class AuthorModelTests(TestCase):
    def test_author_creation(self):
        # Тест создания автора
        author = Author.objects.create(name='John Doe')
        self.assertEqual(author.name, 'John Doe')  # Проверяем, что имя автора соответствует ожидаемому значению
        self.assertEqual(Author.objects.count(), 1)  # Проверяем, что количество авторов равно 1

    def test_author_string_representation(self):
        # Тест строкового представления автора
        author = Author.objects.create(name='John Doe')
        self.assertEqual(str(author), 'John Doe')  # Проверяем, что строковое представление автора соответствует ожидаемому значению


class BookModelTests(TestCase):
    def setUp(self):
        # Устанавливаем начальные данные для тестов
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')
        self.book = Book.objects.create(title='Test Book')

    def test_book_creation(self):
        # Тест создания книги
        self.assertEqual(self.book.title, 'Test Book')  # Проверяем, что название книги соответствует ожидаемому значению
        self.assertEqual(self.book.authors.count(), 0)  # Проверяем, что количество авторов книги равно 0

        self.book.authors.add(self.author1)  # Добавляем автора к книге
        self.book.save()

        self.assertEqual(self.book.authors.count(), 1)  # Проверяем, что количество авторов книги равно 1
        self.assertTrue(self.author1 in self.book.authors.all())  # Проверяем, что добавленный автор присутствует в списке авторов книги

    def test_book_string_representation(self):
        # Тест строкового представления книги
        self.assertEqual(str(self.book), 'Test Book')  # Проверяем, что строковое представление книги соответствует ожидаемому значению