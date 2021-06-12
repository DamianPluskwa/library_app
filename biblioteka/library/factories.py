import factory

from .models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    book_title = factory.Sequence(lambda n: 'Title %s' % n)
    book_author = factory.Sequence(lambda n: 'Author %s' % n)
    book_category = factory.Sequence(lambda n: 'Category %s' % n)
    publication_date = factory.Sequence(lambda n: n + 1900)
