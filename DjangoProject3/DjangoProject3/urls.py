from django.contrib import admin
from django.urls import path
from biblioteka.views import BookListView, shelf_list, shelf_content, DVDListView, user_list, add_user, user_borrowed_items, welcome_view, return_book

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('welcome/', welcome_view, name='welcome'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('shelves/', shelf_list, name='shelf_list'),
    path('shelves/<int:shelf_id>/', shelf_content, name='shelf_content'),
    path('dvd/', DVDListView.as_view(), name='dvd-list'),
    path('users/', user_list, name='user_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/<int:library_card_number>/borrowed/', user_borrowed_items, name='user_borrowed_items'),
    path('books/return/<int:book_id>/', return_book, name='return_book'),
]