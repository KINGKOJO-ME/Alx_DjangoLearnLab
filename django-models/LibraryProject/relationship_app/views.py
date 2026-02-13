from django.shortcuts import render
from .models import Book


def list_books(request):
    #Function-based view that retrieves all books and displays them in a template.

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'relationship_app/list_books.html', context)

from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library
    and list all books available in that library.
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # register view for user registration

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
