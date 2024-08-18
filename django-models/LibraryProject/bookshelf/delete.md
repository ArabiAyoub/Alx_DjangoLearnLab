# Delete Operation for Book

This guide explains the necessary steps to delete a `Book` instance from the database using Django's ORM.

## Import Model

To perform any operation on the `Book` model, it must first be imported:

```python
book.delete()
from bookshelf.models import Book