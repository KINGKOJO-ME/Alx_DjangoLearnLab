from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

# ---------------------------------------------------------
# API URL Configuration
# ---------------------------------------------------------
# These routes map HTTP endpoints to the respective
# generic views that perform CRUD operations.
# ---------------------------------------------------------

urlpatterns = [

    # Retrieve all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update a book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]