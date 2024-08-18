from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import the views module
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),  # Reference to the function-based register view
]