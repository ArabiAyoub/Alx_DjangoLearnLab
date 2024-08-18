from relationship_app.models import Author, Book, Library, Librarian

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