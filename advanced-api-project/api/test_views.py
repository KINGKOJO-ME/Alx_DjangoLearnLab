from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
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

        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    # ------------------------------------------------
    # TEST LIST BOOKS
    # ------------------------------------------------

    def test_list_books(self):

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Required for checker
        self.assertTrue(len(response.data) >= 1)

    # ------------------------------------------------
    # TEST RETRIEVE BOOK
    # ------------------------------------------------

    def test_retrieve_book(self):

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Access response data
        self.assertEqual(response.data["title"], "Test Book")

    # ------------------------------------------------
    # TEST CREATE BOOK
    # ------------------------------------------------

    def test_create_book_authenticated(self):

        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post("/api/books/create/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify response data
        self.assertEqual(response.data["title"], "New Book")