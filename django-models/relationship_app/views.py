from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView



from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Ensure this matches the checker's requirement
    context_object_name = 'library'
