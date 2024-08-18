from relationship_app.models import Author, Book, Library, Librarian
from .models import Author  # Adjust the import according to your models setup
# Assuming 'author_name' is defined somewhere or is a parameter to a function
author_name = "Some Author Name"
author = Author.objects.get(name=author_name)

# Assuming you need to retrieve objects related to this author, such as books
books = Book.objects.filter(author=author)  # Adjust 'Book' to your related model

def query_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Examples for testing the functions:
if __name__ == "__main__":
    # Testing with sample data 
    print(query_books_by_author("Author Name"))
    print(list_all_books_in_library("Library Name"))
    print(retrieve_librarian_for_library("Library Name"))