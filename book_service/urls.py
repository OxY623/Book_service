"""
URL configuration for book_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home

from django.urls import path
from django.contrib import admin
from search_app.views import search
from book_app.views import main_view, \
    books_list, \
    authors_list, \
    add_book, \
    create_author, \
    edit_book, \
    book_detail, \
    author_detail, \
    edit_author, \
    delete_author, \
    delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='home'),
    path('authors/', authors_list, name='authors-list'),
    path('books/', books_list, name='books-list'),
    path('add_book/', add_book, name='add-book'),
    path('create_author', create_author, name='create_author'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('books/<int:book_id>/', book_detail, name='book-detail'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('author/<int:author_id>/edit/', edit_author, name='edit_author'),
    path('author/<int:author_id>/delete/', delete_author, name='delete_author'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
    path('search/', search, name='search'),
]


