from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView  # Ensure RegisterView is imported correctly

urlpatterns = [
    # Use LoginView with a specified template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Use LogoutView and specify the next page
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='login'), name='logout'),

    # Reference to RegisterView for registration
    path('register/', RegisterView.as_view(), name='register'),
]