"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'myapp/templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_h1gu0ypjysy1flz5vieyx$8i7)84y^4zo=ypd2qtapxkui%jf'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'myapp.blog',
    'myapp.coding',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'markdownx',
    'treebeard',
]

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.codehilite',
    'markdown.extensions.fenced_code',
    'markdown.extensions.extra',
    'markdown.extensions.toc'
]

MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {
    'markdown.extensions.codehilite': {
        'linenums': True,
        'use_pygments': True,
        'noclasses': True
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyblog', #데이터베이스명
        'USER': 'pyblog',
        'PASSWORD': '2150',
        # 현재 호스트(IP)가 유동 IP라서 AWS 재시동시 수정해야 함.
        'HOST': '52.79.177.203',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myapp/static')]
STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.FileSystemFinder", "django.contrib.staticfiles.finders.AppDirectoriesFinder",]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'myapp/media')

LOGGING = {
    'version' : 1,
    'disable_existing_loggers': False,
    # 형식정의
    'formatters': {
        'format1': {'format': '[%(asctime)s] %(levelname)s %(message)s','datefmt': "%Y-%m-%d %H:%M:%S"},
        'format2': {'format': '%(levelname)s %(message)s [%(name)s:%(lineno)s]'},
    },
    'handlers': {
        # 파일저장
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/pythonblog.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5, # 백업파일 5개
            'formatter': 'format1',
        },
        # 콘솔(터미널)에 출력
        'console': {'level': 'INFO','class': 'logging.StreamHandler','formatter': 'format2',
                    },
    },
    'loggers': {
        # 종류
        'django.server': {
            'handlers': ['file','console'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.request': {
            'handlers':['file','console'],
            'propagate': False,
            'level':'DEBUG',
        },        
        '': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True,
        },
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
