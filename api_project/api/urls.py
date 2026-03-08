from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


# Router automatically creates CRUD routes
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [

    # Existing endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Router endpoints
    path('', include(router.urls)),
]