from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Secure form for creating and updating Book objects.
    Django forms automatically validate and sanitize input,
    helping prevent SQL injection and other malicious input.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 2:
            raise forms.ValidationError("Title must contain at least 2 characters.")

        return title