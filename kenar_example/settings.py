"""
Django settings for kenar_example project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ptdgn^0%lglx$h40i7d%bny0p=*im6lb3+(iu5_=@r^@c8kvwv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["kenar-example.darkube.app", "localhost", "ef7e-16-24-70-196.ngrok-free.app"]

CSRF_TRUSTED_ORIGINS = ['https://kenar-example.darkube.app', 'http://localhost:8000', 'http://127.0.0.1:8000']

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_NAME = os.getenv("DATABASE_NAME", "kenar_new")
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tech_check',
    'chat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kenar_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'kenar_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DIVAR_APP_SLUG = "mire-sulpher-elf"
DIVAL_OAUTH_REDIRECT_URL = "https://open-platform-redirect.divar.ir/oauth"
APP_BASE_URL = "https://kenar-example.darkube.app"
DIVAR_FALLBACK_REDIRECT_URL = f"{APP_BASE_URL}/oauth/callback"
CHAT_FALLBACK_REDIRECT_URL = f"{APP_BASE_URL}/chat/oauth/callback"
DIVAR_API_KEY = ("45kFWH2rsoQKBeZRWTYb5pleDGn16KS8dNLaM3cXWC63XESkeQYiOJaAC8vpxJkB"
                 "xaQJ2UQ9Ce2YOV6WwLiI313xpPqYWSvtcF6JPGHW9DzwnrTI1ZBrIT4f0Ip9HPqup"
                 "5HfQmyCqQMslCFl2kVBysSZYXFdtDbWEGtU0R47V8KdwFUwFaKh3TtASNQ4MKvMsod"
                 "Sf6iyJqvqhTRl7DUOmRS62JaNLVg142EfBcNFJ0Ypl2HhOhLnW6pQn8U8pyiq")
DIVAR_OAUTH_ACCESS_TOKEN_URL = "https://api.divar.ir/v1/open-platform/oauth/access_token"
DIVAR_API_BASE_URL = "https://api.divar.ir"