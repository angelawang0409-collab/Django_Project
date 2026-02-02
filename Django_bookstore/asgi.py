# Imports the os module to work with environment variables and file paths
import os

# Imports Django’s ASGI application function for asynchronous servers
from django.core.asgi import get_asgi_application

# Sets the default Django settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_bookstore.settings')

# Creates the ASGI application object that the web server uses to communicate with Django
application = get_asgi_application()
