# -*- coding: utf-8 -*-

from .base import * # noqa


DEBUG = True
ALLOWED_HOSTS = ['192.168.33.10']

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_PORT = 1025

# Django Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']                                 # noqa
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']   # noqa
INTERNAL_IPS = ['127.0.0.1', '192.168.33.1']
