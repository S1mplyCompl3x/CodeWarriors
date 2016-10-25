import os
import environ
import dj_database_url

BASE = os.path.abspath(os.path.dirname(__name__))

env = environ.Env()

DATABASES = {
}
DATABASES['default'] = dj_database_url.config(default='DATABASE_URL')

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Residency_local',
        'USER': 'Residency_local',
        'PASSWORD': 'Residency_local',
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}'''

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'Residency'
    }
}

RAVEN_CONFIG = {
    'dsn': ""
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedFileSystemStorage'

STATIC_URL = "/static/"

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'

BASE_URL = "http://local.Residency.com"
