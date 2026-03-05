from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


def book_list(request):
    """
    Displays all books stored in the database.
    Uses Django ORM instead of raw SQL to prevent SQL injection.
    """

    books = Book.objects.all()

    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('bookshelf.can_create', raise_exception=True)
def form_example(request):
    """
    Demonstrates secure form handling with Django forms.
    Protects against malicious input through built-in validation.
    """

    if request.method == "POST":
        form = ExampleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            publication_year = form.cleaned_data["publication_year"]

            # Using Django ORM prevents SQL injection
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year
            )

    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})