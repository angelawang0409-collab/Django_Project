
# Import the path function from Django's URL routing system
# path() is used to define URL patterns and map them to views
from django.urls import path

# Import the SignUpView class-based view from the current app's views module
# The dot (.) indicates it's in the same package/directory
from .views import SignUpView

# Define the URL patterns for this app
# urlpatterns is a list that Django uses to match incoming URLs to views
urlpatterns = [
    # Define a URL pattern for the signup page
    # 'accounts/' - The URL path that users will visit (e.g., http://example.com/accounts/)
    # SignUpView.as_view() - Converts the class-based view to a view function
    # name='signup' - A unique name for this URL pattern, used for reverse URL lookup
    path('accounts/', SignUpView.as_view(), name='signup'),
]