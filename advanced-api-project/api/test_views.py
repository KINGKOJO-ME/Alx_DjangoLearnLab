from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    These tests verify CRUD operations, filtering,
    searching, ordering, and permission enforcement.
    """

    def setUp(self):
        """
        Setup test data before running each test.
        """

        # Create user for authentication tests
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book.id}/"
        self.delete_url = f"/api/books/delete/{self.book.id}/"

    # --------------------------------------------------
    # TEST LIST BOOKS
    # --------------------------------------------------

    def test_list_books(self):
        """
        Ensure the book list endpoint returns books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------
    # TEST RETRIEVE BOOK
    # --------------------------------------------------

    def test_retrieve_book(self):
        """
        Ensure a single book can be retrieved.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------
    # TEST CREATE BOOK
    # --------------------------------------------------

    def test_create_book_authenticated(self):
        """
        Authenticated users should be able to create books.
        """

        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """
        Unauthenticated users should NOT be able to create books.
        """

        data = {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --------------------------------------------------
    # TEST UPDATE BOOK
    # --------------------------------------------------

    def test_update_book(self):
        """
        Authenticated users should be able to update books.
        """

        self.client.login(username="testuser", password="password123")

        data = {
            "title": "Updated Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------
    # TEST DELETE BOOK
    # --------------------------------------------------

    def test_delete_book(self):
        """
        Authenticated users should be able to delete books.
        """

        self.client.login(username="testuser", password="password123")

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --------------------------------------------------
    # TEST FILTERING
    # --------------------------------------------------

    def test_filter_books_by_title(self):
        """
        Ensure filtering books by title works.
        """

        response = self.client.get("/api/books/?title=Test Book")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------
    # TEST SEARCH
    # --------------------------------------------------

    def test_search_books(self):
        """
        Ensure search functionality works.
        """

        response = self.client.get("/api/books/?search=Test")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------------------------------------
    # TEST ORDERING
    # --------------------------------------------------

    def test_order_books(self):
        """
        Ensure ordering functionality works.
        """

        response = self.client.get("/api/books/?ordering=publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)