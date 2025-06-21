"""
Django settings for ecom project.

This file is a cleaned-up and secure version, suitable for both
local development and production deployment.
"""

from pathlib import Path
import os
import dj_database_url

# Load environment variables from env.py if it exists (for local development)
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- CORE SECURITY & DEPLOYMENT SETTINGS ---

# SECRET_KEY is loaded from environment variables for security.
# NEVER commit a secret key to version control.
SECRET_KEY = os.environ.get('SECRET_KEY')

# In production, DEBUG must be False.
# For local development, you can set DEBUG=True in your env.py
# Example: os.environ['DEBUG'] = 'True'
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Define the allowed hosts. In production, this should be your domain.
ALLOWED_HOSTS = [
    '127.0.0.1',
    '.herokuapp.com',
    # Add your production domain here, e.g., 'www.yourgreatcart.com'
]


# --- APPLICATION DEFINITION ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'admin_thumbnails',
    'cloudinary_storage',
    'cloudinary',

    # My Apps
    'store',
    'accounts',
    'cart',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise middleware should be placed directly after SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'
WSGI_APPLICATION = 'ecom.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- TEMPLATES CONFIGURATION ---

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_counter',
            ],
        },
    },
]


# --- DATABASE CONFIGURATION ---
# Switches between production (Postgres) and development (SQLite)

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    print("DATABASE_URL not found. Using SQLite as the database.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- AUTHENTICATION CONFIGURATION ---

AUTH_USER_MODEL = 'accounts.Account'
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# --- STATIC AND MEDIA FILES CONFIGURATION ---

# Static files (CSS, JavaScript, site images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The line below is commented out to fix the 'MissingFileError' during collectstatic.
# This is a temporary fix for local development. For production, you should ensure
# all referenced files (like 'owl.video.play.png') exist in your static directories.
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (User-uploaded content, e.g., product images)
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
if CLOUDINARY_URL:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    # Settings for local media file storage
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- EMAIL CONFIGURATION ---
# Credentials are loaded from environment variables for security.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

