# Imports Django’s admin module for the built-in admin interface
from django.contrib import admin
# Imports functions for defining URL patterns
from django.urls import path, include
# Imports Django’s built-in authentication views (login/logout)
from django.contrib.auth import views as auth_views
# Imports the project settings to access MEDIA_URL and MEDIA_ROOT
from django.conf import settings
# Imports the static() helper to serve media files during development
from django.conf.urls.static import static


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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adds URL patterns to serve media files (user-uploaded files) during development
# Maps MEDIA_URL (e.g., /media/) to the folder defined in MEDIA_ROOT so uploaded images can be accessed

