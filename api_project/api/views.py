from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# ---------------------------------------------------------
# BookList View
# ---------------------------------------------------------
# Returns a list of all books.
# This endpoint is used for simple GET requests.
# ---------------------------------------------------------

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ---------------------------------------------------------
# BookViewSet
# ---------------------------------------------------------
# ModelViewSet provides full CRUD functionality:
#
# list()      -> GET /books_all/
# retrieve()  -> GET /books_all/<id>/
# create()    -> POST /books_all/
# update()    -> PUT /books_all/<id>/
# destroy()   -> DELETE /books_all/<id>/
# ---------------------------------------------------------

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer