\# Create Book Instance



```python

from bookshelf.models import Book



book = Book(title="1984", author="George Orwell", publication\_year=1949)

book.save()



Book.objects.all()  # <QuerySet \[<Book: 1984 by George Orwell (1949)>]>

