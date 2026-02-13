from django.shortcuts import render
from .models import Book


def list_books(request):
    #Function-based view that retrieves all books and displays them in a template.

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'relationship_app/list_books.html', context)

from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library
    and list all books available in that library.
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # register view for user registration

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # for register view

urlpatterns = [
    path('register/', views.register, name='register'),
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
]
