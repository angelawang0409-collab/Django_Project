# Imports Django’s admin module for the built-in admin interface
from django.contrib import admin
# Imports functions for defining URL patterns
from django.urls import path, include
# Imports Django’s built-in authentication views (login/logout)
from django.contrib.auth import views as auth_views

# Defines all URL patterns for the project
urlpatterns = [
    # URL for the admin site
    path('admin/', admin.site.urls),
    # URL for the login page using Django’s built-in LoginView
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # URL for the logout page using Django’s built-in LogoutView
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Root URL includes all URLs from the books app and assigns a namespace
    path('', include('books.urls', namespace='books'))
]

