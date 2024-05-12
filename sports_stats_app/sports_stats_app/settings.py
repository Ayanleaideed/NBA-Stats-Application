import os
from pathlib import Path
from datetime import datetime, timedelta
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # reads the .env file

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security and debugging settings
SECRET_KEY = env('SECRET_KEY', default='django-insecure-z_zde1*fk)*_k$-cpoi)r-cb%23)y%=0j@n8h2tbou0be6^52#')
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = [
    'nba-stats-application.vercel.app',
    'nba-stats-application-az7d11yrf-ayanles-projects-abda602c.vercel.app',
    '.vercel.app',
    '127.0.0.1',
    'localhost'
]

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stats.apps.StatsConfig',
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'sports_stats_app.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI application path
WSGI_APPLICATION = 'sports_stats_app.wsgi.application'

# Database configuration
DATABASES = {
    'default': env.db(),
}

# Session configuration
now = datetime.now()
midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
seconds_until_midnight = (midnight - now).seconds
SESSION_COOKIE_AGE = seconds_until_midnight
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
