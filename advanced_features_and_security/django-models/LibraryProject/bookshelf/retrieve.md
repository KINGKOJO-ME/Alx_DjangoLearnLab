\# Retrieve Book Instance



```python

from bookshelf.models import Book



book = Book.objects.get(title="1984")

print(book)

\# Output: 1984 by George Orwell (1949)



