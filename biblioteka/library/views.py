from django.shortcuts import render, get_object_or_404
from .models import Book, Rent

# Create your views here.


def available_book_list(request):
    books = Book.objects.filter(book_available=True)

    return render(
        request,
        "library/list.html",
        {"books": books},
    )


def rented_list(request):
    rented_books = Rent.objects.all()

    return render(
        request,
        "library/rented_list.html",
        {"rented_books": rented_books},
    )


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(
        request,
        "library/detail.html",
        {"book": book}
    )


def rent(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.book_available = False
    book.rent_set.create()
    book.save()

    return render(
        request,
        "library/rent.html",
        {"book": book}
    )


def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.book_available = True
    book.save()

    r = book.rent_set.filter(book_id=book_id)
    r.delete()

    return render(
        request,
        "library/returned_book.html",
        {"book": book}
    )
