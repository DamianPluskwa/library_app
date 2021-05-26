from django.db import models

# Create your models here.


class Book(models.Model):

    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200)
    publication_date = models.IntegerField()

    book_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book_title} {self.book_author} {self.book_category} {self.publication_date}"


class Rent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    rent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book} Wypożyczono {self.rent_date}"
