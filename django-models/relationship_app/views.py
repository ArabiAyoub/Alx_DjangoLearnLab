from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def list_books(request):
    books = Book.objects.all()
    content = '<h1>Books Available:</h1><ul>'
    for book in books:
        content += f'<li>{book.title} by {book.author.name}</li>'
    content += '</ul>'
    return HttpResponse(content)