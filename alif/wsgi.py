"""
WSGI config for alif project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'alif.azure' if 'https://arabic-test1webapp.azurewebsites.net/' in os.environ else 'alif.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
