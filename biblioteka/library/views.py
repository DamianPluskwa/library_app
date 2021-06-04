from django.shortcuts import render, get_object_or_404
from .models import Book, Rent, Rating, CopiesOfBooks
from .forms import SearchForm, RatingForm


# Create your views here.


def available_book_list(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            if form.cleaned_data["search_category"] == 'title':
                books = Book.objects.filter(book_title__contains=form.cleaned_data["search_text"], book_available=True)
            elif form.cleaned_data["search_category"] == 'author':
                books = Book.objects.filter(book_author__contains=form.cleaned_data["search_text"], book_available=True)
            elif form.cleaned_data["search_category"] == 'category':
                books = Book.objects.filter(book_category__contains=form.cleaned_data["search_text"],
                                            book_available=True)

            return render(
                request,
                "library/list.html",
                {"books": books,
                 "form": form}
            )
    else:
        books_all = Book.objects.all()
        books = []
        for book in books_all:
            if book.book_available:
                books.append(book)
        form = SearchForm()

    return render(
        request,
        "library/list.html",
        {"books": books,
         "form": form}
    )


def rented_list(request):
    rented_books = Rent.objects.all()
    return render(
        request,
        "library/rented_list.html",
        {"rented_books": rented_books},
    )


def detail(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        rent_books = Rent.objects.filter(book_id=book_id)
        form = RatingForm(request.POST)
        if form.is_valid():
            book.rating_set.create(number=form.cleaned_data["number_value"])
            user_value = form.cleaned_data["number_value"]
            book.save()

            return render(
                request,
                "library/detail.html",
                {"book": book,
                 "form": form,
                 "user_value": user_value,
                 "rent_books": rent_books
                 }
            )
    else:
        book = get_object_or_404(Book, pk=book_id)
        rent_books = Rent.objects.filter(book_id=book_id)
        form = RatingForm()

    return render(
        request,
        "library/detail.html",
        {"book": book,
         "form": form,
         "rent_books": rent_books
         }
    )


def rent(request, book_id):
    book_object = get_object_or_404(Book, pk=book_id)
    book_copies = get_object_or_404(CopiesOfBooks, book=book_object)
    book_copies.available -= 1
    book_object.rent_set.create()
    book_object.save()
    book_copies.save()

    return render(
        request,
        "library/rent.html",
        {"book": book_object}
    )


def return_book(request, book_id):
    book_object = get_object_or_404(Book, pk=book_id)
    book_copies = get_object_or_404(CopiesOfBooks, book=book_object)
    book_copies.available += 1
    book_object.save()
    book_copies.save()

    r = book_object.rent_set.filter(book_id=book_id)
    r.delete()

    return render(
        request,
        "library/returned_book.html",
        {"book": book_object}
    )
