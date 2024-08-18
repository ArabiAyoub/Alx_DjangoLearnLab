from django.urls import path
from .views import RegisterView, custom_login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', custom_login_view, name='login'),  # Use custom login view
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]