from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


# ---------------------------------------------------------
# Book List View
# ---------------------------------------------------------
# This view retrieves a list of all books in the database.
#
# Permissions:
# - Anyone can read the list of books.
# - Authenticated users can create new books.
#
# Generic View Used:
# ListCreateAPIView
# Combines:
#   - ListAPIView
#   - CreateAPIView
# ---------------------------------------------------------

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------------------------------------
# Book Detail View
# ---------------------------------------------------------
# This view retrieves a single book instance based on
# the primary key (ID).
#
# Generic View Used:
# RetrieveAPIView
# ---------------------------------------------------------

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------------------------------------
# Book Create View
# ---------------------------------------------------------
# Handles creation of new Book objects.
#
# Only authenticated users can create books.
# ---------------------------------------------------------

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------------------------------------
# Book Update View
# ---------------------------------------------------------
# Allows updating an existing Book object.
#
# Only authenticated users are allowed to update books.
# ---------------------------------------------------------

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------------------------------------
# Book Delete View
# ---------------------------------------------------------
# Allows deletion of a Book object.
#
# Only authenticated users can delete books.
# ---------------------------------------------------------

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]