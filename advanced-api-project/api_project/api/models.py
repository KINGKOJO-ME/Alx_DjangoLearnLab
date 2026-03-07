from django.db import models

# -------------------------------------------------------------
# Book Model
# -------------------------------------------------------------
# This model represents a simple book entity that will later
# be exposed through a Django REST Framework API.
#
# Fields:
# title  -> stores the title of the book
# author -> stores the author's name
#
# This model is intentionally simple for the introductory API task.
# -------------------------------------------------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title