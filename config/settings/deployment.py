from config.settings.common import *
import os


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = False

ALLOWED_HOSTS = [
    "localhost",  # Replace with server host
]
