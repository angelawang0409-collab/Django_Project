# Project information and required imports for Django configuration
import os
from pathlib import Path

# Defines the base directory of the project to help locate files and folders
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings including secret key, debug mode, and allowed hosts
# Keep SECRET_KEY private in production and set DEBUG to False for live websites
SECRET_KEY = '4c!5dmr29c&9d(5#ekg%51_0b+5-pagr!&i((1==-5zoz$h^8^'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition listing all installed apps including Django defaults and custom apps
# These apps provide features like admin, authentication, sessions, messaging, and static files
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books.apps.BooksConfig',
    'accounts.apps.AccountsConfig',
]

# Middleware configuration which processes requests and responses globally
# Middleware provides security, session handling, authentication, and other features
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration for mapping URLs to views
ROOT_URLCONF = 'Django_bookstore.urls'

# Template settings that define how HTML templates are loaded and rendered
# Includes directories to search for templates and context processors to provide data
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application path for deploying the project to a web server
WSGI_APPLICATION = 'Django_bookstore.wsgi.application'

# Database configuration using SQLite for local development
# Can be replaced with other databases like PostgreSQL or MySQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation settings to enforce strong passwords
# Prevents easy-to-guess passwords and improves user security
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings for language, timezone, and formatting
# Makes the project suitable for users in different regions
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings for CSS, JavaScript, and images
# STATIC_URL defines the URL path, STATICFILES_DIRS are local static folders
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
# Sets the URL path prefix for serving media files (user-uploaded files)
MEDIA_URL = '/media/'

# Defines the folder on your computer where uploaded media files are stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Login and logout settings including URLs for authentication
# LOGIN_REDIRECT_URL defines where users go after login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
