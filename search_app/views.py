from django.shortcuts import render

# Create your views here.
from book_app.models import Book


def search(request):
    query = request.GET.get('query')

    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(authors__name__icontains=query)
    else:
        books = []

    context = {'books': books, 'query': query}

    return render(request, 'search_results_book.html', context)
