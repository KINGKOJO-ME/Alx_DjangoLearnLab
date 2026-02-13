from django.shortcuts import render
from .models import Book


def list_books(request):
    #Function-based view that retrieves all books and displays them in a template.

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'relationship_app/list_books.html', context)

from django.views.generic import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library
    and list all books available in that library.
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
