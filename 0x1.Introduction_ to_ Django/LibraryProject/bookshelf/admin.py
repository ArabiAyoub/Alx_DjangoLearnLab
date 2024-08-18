from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')  # Enables filtering by these fields
    search_fields = ('title', 'author__name')  # Enables searching by title and author name

admin.site.register(Book, BookAdmin)