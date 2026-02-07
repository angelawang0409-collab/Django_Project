# Specifies that this script should be run using the system's Python interpreter
#!/usr/bin/env python

# Provides a brief description of the file's purpose
"""Django's command-line utility for administrative tasks."""
# Imports the os module to interact with the operating system
import os
# Imports the sys module to access command-line arguments
import sys


# Defines the main function that runs Django administrative commands
def main():
    # Sets the default Django settings module for the project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_bookstore.settings')
    try:
        # Imports Django’s command-line execution function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raises an error if Django is not installed or not accessible
        raise ImportError(
            # Error message explaining the possible cause of the issue
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    # Executes the Django command using the provided command-line arguments
    execute_from_command_line(sys.argv)


# Checks if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    # Calls the main function to start the Django command-line utility
    main()

