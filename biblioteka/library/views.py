from django.shortcuts import render, get_object_or_404
from .models import Book, Rent
from .forms import SearchForm


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
        books = Book.objects.filter(book_available=True)
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
