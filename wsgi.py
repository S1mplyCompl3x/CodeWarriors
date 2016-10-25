"""
WSGI config for newdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Residency.settings")
# test if environment variable is properly set
# print(os.environ.get('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()
