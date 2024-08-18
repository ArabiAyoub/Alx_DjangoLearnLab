# Create Operation

This section demonstrates how to create a new `Book` instance using the `Book.objects.create()` method and save it to the database directly.

**Command:**
```python
from bookshelf.models import Book

# Creating and saving a new Book instance in one step
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)