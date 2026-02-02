# Import the AppConfig class from Django's apps module
# AppConfig is used to configure application-specific settings
from django.apps import AppConfig


# Define the configuration class for the 'accounts' application
# This class inherits from Django's AppConfig base class
class AccountsConfig(AppConfig):
    # Set the name of the application
    # This should match the name of the app's directory
    # Django uses this to identify and register the app
    name = 'accounts'