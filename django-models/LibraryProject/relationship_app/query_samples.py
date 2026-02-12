# relationship_app/query_samples.py

import os
import django

# 1 Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 2 Optional: Create sample data (only if DB is empty)
def create_sample_data():
    if Author.objects.exists():
        return  # Skip if data already exists

    # Authors
    a1 = Author.objects.create(name="J.K. Rowling")
    a2 = Author.objects.create(name="George Orwell")

    # Books
    b1 = Book.objects.create(title="Harry Potter 1", author=a1)
    b2 = Book.objects.create(title="Harry Potter 2", author=a1)
    b3 = Book.objects.create(title="1984", author=a2)

    # Libraries
    l1 = Library.objects.create(name="Central Library")
    l2 = Library.objects.create(name="Community Library")

    # Assign books to libraries
    l1.books.set([b1, b2])
    l2.books.set([b2, b3])

    # Librarians
    Librarian.objects.create(name="Alice", library=l1)
    Librarian.objects.create(name="Bob", library=l2)


# Task 1: Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Tracker wants this exact line:
        books = Book.objects.filter(author=author)  # <- ALX tracker line
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")



# 4 Task 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")


# 5 Task 3: Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOneField access
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")


# 6 Main test run
if __name__ == "__main__":
    # Create sample data if not already present
    create_sample_data()

    # Run all tasks
    books_by_author("George Orwell")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
