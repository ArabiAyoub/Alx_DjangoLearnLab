from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import the views module

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='login'), name='logout'),
    path('register/', views.register, name='register'),  # Reference to the function-based register view
]