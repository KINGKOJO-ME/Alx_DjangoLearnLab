from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def add_book(request):
    """
    View to securely create a new book using Django forms.
    """

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})