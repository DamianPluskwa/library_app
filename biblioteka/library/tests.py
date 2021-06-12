from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .factories import BookFactory
from .models import Book


class TestViewsRentedList(TestCase):
    def test_(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Powrót do listy dostępnych książek.')

    def test_3(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Brak dostępnych książek')
        self.assertNotContains(response, 'Minęła data zwrotu.')

    def test_4(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)


class TestBookModel(TestCase):
    def test_book_available_true(self):
        new_book = Book(book_title="", book_author="", book_category="", publication_date=1900)
        new_book.save()
        copies_new_book = new_book.copiesofbooks_set.create(copies=2, available=2)
        copies_new_book.save()

        self.assertIs(new_book.book_available, True)

    def test_book_available_false(self):
        new_book = Book(book_title="", book_author="", book_category="", publication_date=1900)
        new_book.save()
        copies_new_book = new_book.copiesofbooks_set.create(copies=2, available=0)
        copies_new_book.save()

        self.assertIs(new_book.book_available, False)


class TestBookModelFixtures(TestCase):
    fixtures = ["library/fixtures/books.json"]

    def test_get_all_books(self):
        self.assertEqual(Book.objects.count(), 7)
        self.assertEqual(Book.objects.filter(book_title__contains="Harry Potter").first().id, 3)

    def test_get_book(self):
        book = BookFactory()
        self.assertEqual(book.book_title, "Title 0")
        book_2 = BookFactory()
        self.assertEqual(book_2.book_title, "Title 1")

    def test_get_ten_books(self):
        books = [BookFactory() for _ in range(10)]
        self.assertEqual(books[1].book_title, "Title 3")
