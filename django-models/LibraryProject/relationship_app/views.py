from django.shortcuts import render
from .models import Book


def list_books(request):
    #Function-based view that retrieves all books and displays them in a template.

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'relationship_app/list_books.html', context)
