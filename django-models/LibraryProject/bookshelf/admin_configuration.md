# Configuring Django Admin for Book Model

## Registration of Book Model

The `Book` model is registered with the Django admin to enable its management through the admin panel. This is done in the `bookshelf/admin.py` file:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)