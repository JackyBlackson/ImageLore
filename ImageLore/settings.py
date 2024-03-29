"""
Django settings for ImageLore project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import ImageLore.site_config as site_config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--bq6!^_z85xb#mf+6d18r*7@dguy$fdevdgcfxcfba=3ehhy@*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_DJANGO_STATIC_FILE_SERVICE = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ALLOWED_HOSTS = [
    "frontend",
    "localhost",
    "127.0.0.1",
    "r7qbur.natappfree.cc",
    'jacky-blackon.natapp1.cc',
    '121.40.90.193',
    site_config.SITE_HOST
]

CSRF_TRUSTED_ORIGINS = [
    'http://jacky-front.natapp1.cc',
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    'http://121.40.90.193:3000',
    "http://127.0.0.1",
    "http://localhost",
    "http://nginx:80",
    "http://nginx"
]
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    'http://jacky-front.natapp1.cc',
    'http://121.40.90.193:3000',
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1",
    "http://localhost",
    "http://nginx:80",
    "http://nginx"
]
INTERNAL_IPS = [
    "127.0.0.1"
]
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False

CORS_ALLOW_HEADERS = [
    'xsrfheadername',
    'xsrfcookiename',
    'content-type',
    'x-csrftoken',
    'X-CSRFTOKEN',
]

CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    "UserAndPermission.apps.UserandpermissionConfig",
    "ImageLoreCoreApp.apps.ImagelorecoreappConfig",
    "ImageLoreFrontEnd.apps.ImagelorefrontendConfig",
    'dj_rest_auth',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ImageLore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ImageLoreFrontEnd.context_processors.custom_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'ImageLore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # 每页显示的对象数量
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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
