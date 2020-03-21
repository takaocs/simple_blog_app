# -*- coding: utf-8 -*-

from .base import * # noqa


DEBUG = False
ALLOWED_HOSTS = ['192.168.33.10']

# Email
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_PORT = 1025

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'ATOMIC_REQUESTS': True
    }
}

# Media
MEDIA_ROOT = str(ROOT_DIR.path('media', 'test'))
