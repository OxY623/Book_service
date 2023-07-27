from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import BookForm, AuthorForm


def main_view(request):
    books_count = Book.objects.count()
    authors_count = Author.objects.count()
    context = {
        'books_count': books_count,
        'authors_count': authors_count,
    }
    return render(request, 'home.html', context)


def books_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books_list.html', context)


def authors_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authors_list.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'add_book.html', context)


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors-list')
    else:
        form = AuthorForm()
    context = {'form': form}
    return render(request, 'create_author.html', context)

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    context = {'form': form, 'book': book}
    return render(request, 'edit_book.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'book-detail.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.book_set.all()
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author_detail.html', context)


def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm(instance=author)

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'edit_author.html', context)


def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('authors-list')

    context = {
        'author': author
    }
    return render(request, 'delete_author.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('books-list')
    context = {
        'book': book
    }

    return render(request, 'delete_book.html', context)