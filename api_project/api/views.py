from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


# API view to list all books
# Uses DRF's ListAPIView to return a queryset of Book objects
class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer