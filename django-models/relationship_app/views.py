from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate  # Include authenticate for manual login handling
from .models import UserProfile

def role_check(role):
    def check(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return check

@user_passes_test(role_check('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(role_check('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(role_check('Member'))
def member_view(request):
    return render(request, 'member_view.html')
# Custom login view (if needed)
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_success_url')  # Redirect to a success page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration