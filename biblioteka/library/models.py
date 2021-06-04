import datetime

from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200)
    publication_date = models.IntegerField()

    def __str__(self):
        return f"{self.book_title} {self.book_author} {self.book_category} {self.publication_date}"

    @property
    def book_available(self):
        book_copies = get_object_or_404(CopiesOfBooks, book=self)
        if book_copies.available > 0:
            return True
        else:
            return False


class Rent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    rent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book} Wypożyczono {self.rent_date}"

    def the_deadline_for_return_has_expired(self) -> bool:
        return self.rent_date < timezone.now() - datetime.timedelta(weeks=2)


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.book} Ocena: {self.number}"


class CopiesOfBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return f"{self.book} Copies: {self.copies} Available: {self.available}"
