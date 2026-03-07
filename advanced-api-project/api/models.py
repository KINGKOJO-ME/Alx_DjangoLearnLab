from django.db import models


# -------------------------------------------------------
# Author Model
# -------------------------------------------------------
# This model represents a book author.
# Each author can write multiple books.
# This creates a one-to-many relationship between
# Author and Book.
# -------------------------------------------------------

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# -------------------------------------------------------
# Book Model
# -------------------------------------------------------
# This model represents a book written by an author.
#
# Fields:
# title -> title of the book
# publication_year -> year the book was published
# author -> foreign key linking the book to its author
#
# Relationship:
# One Author -> Many Books
# -------------------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title