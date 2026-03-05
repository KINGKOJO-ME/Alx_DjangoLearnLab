from django import forms
from .models import Book


class ExampleForm(forms.Form):
    """
    Example form used to demonstrate secure handling of user input.
    Django automatically validates and sanitizes the input fields.
    """

    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    publication_year = forms.IntegerField()


class BookForm(forms.ModelForm):
    """
    ModelForm connected to the Book model.
    It allows users to safely create Book objects using Django's ORM.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']