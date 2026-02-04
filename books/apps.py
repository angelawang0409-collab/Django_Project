# Import AppConfig from Django's application registry system
from django.apps import AppConfig


# Define the configuration class for the 'books' Django application
class BooksConfig(AppConfig):
    # Set the name of the application (must match the app directory name)
    # Django uses this to identify and register the app in INSTALLED_APPS
    name = 'books'
