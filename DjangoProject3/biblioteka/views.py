import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Book, Shelf, DVD, User
from .forms import UserForm, BookBorrowForm, DVDBorrowForm


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class DVDListView(ListView):
    model = DVD
    template_name = "books/dvd_list.html"
    context_object_name = "DVD"

def shelf_list(request):
    shelves = Shelf.objects.all()
    return render(request, 'books/shelf_list.html', {'shelves': shelves})


def shelf_content(request, shelf_id):
    shelf = get_object_or_404(Shelf, pk=shelf_id)
    books = Book.objects.filter(shelf=shelf)
    dvds = DVD.objects.filter(shelf=shelf)

    return render(request, 'books/shelf_content.html', {'shelf': shelf, 'books': books, 'dvds': dvds})

def user_list(request):
    users = User.objects.all()
    return render(request, 'books/user_list.html', {'users': users})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'books/add_user.html', {'form': form})


def user_borrowed_items(request, library_card_number):
    user = get_object_or_404(User, pk=library_card_number)
    books = Book.objects.filter(borrowed_by=user)
    dvds = DVD.objects.filter(borrowed_by=user)

    # Formularz wypożyczenia książki
    if request.method == "POST":
        if 'book_form' in request.POST:
            book_form = BookBorrowForm(request.POST)
            if book_form.is_valid():
                book = book_form.cleaned_data['book']
                book.borrowed_by = user
                book.borrowed_date = datetime.date.today()
                book.is_borrowed = True
                book.save()
                return redirect('user_borrowed_items', library_card_number=library_card_number)
        elif 'dvd_form' in request.POST:
            dvd_form = DVDBorrowForm(request.POST)
            if dvd_form.is_valid():
                dvd = dvd_form.cleaned_data['dvd']
                dvd.borrowed_by = user
                dvd.borrowed_date = datetime.date.today()
                dvd.is_borrowed = True
                dvd.save()
                return redirect('user_borrowed_items', library_card_number=library_card_number)
    else:
        book_form = BookBorrowForm()
        dvd_form = DVDBorrowForm()

    return render(request, 'books/user_borrowed_items.html', {
        'user': user,
        'books': books,
        'dvds': dvds,
        'book_form': book_form,
        'dvd_form': dvd_form,
    })

def welcome_view(request):
    return render(request, 'books/welcome_view.html')


def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.is_borrowed:
        book.borrowed_by = None
        book.borrowed_date = None
        book.is_borrowed = False
        book.save()

    return redirect('book-list')