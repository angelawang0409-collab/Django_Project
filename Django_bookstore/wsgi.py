# Imports the os module to interact with the operating system
import os

# Imports Django’s function to get the WSGI application
from django.core.wsgi import get_wsgi_application

# Sets the default Django settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_bookstore.settings')

# Creates the WSGI application object that the web server uses to communicate with Django
application = get_wsgi_application()