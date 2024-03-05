import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = ['SECRET']
ALLOWED_HOSTS=[os.environ['https://arabic-test1webapp.azurewebsites.net/']]
CSRF_TRUSTED_ORIGINS = ['https://arabic-test1webapp.azurewebsites.net/']
DEBUG = False
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR,'static')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "arabic",
        "USER": "shazil",
        "PASSWORD": "Sh@zil1286rrr",
        "HOST": "arabic-dbserver.postgres.database.azure.com",
        "PORT": "5432",
    }
}