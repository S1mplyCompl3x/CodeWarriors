# -*- coding: utf-8 -*-

DEBUG = env.bool('DJANGO_DEBUG', True)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["..com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Residency',
        'USER': 'Residency',
        'PASSWORD': 'Residency',
        'HOST': '127.0.0.1',
        'PORT': '8080',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedS3BotoStorage'

# Optionally change to full CDN url
STATIC_URL = "/static/"

BASE_URL = "https://Residency.com"
