from .common import *
import os
import dj_database_url

# Update the database configuration with dj-database-url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Allow all host headers
ALLOWED_HOSTS = ['.herokuapp.com']

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://*.herokuapp.com",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.extend([
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
])

# Security settings for production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Ensure you have the correct settings for static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Secret key configuration
SECRET_KEY = os.environ.get('SECRET_KEY')

# Debug mode
DEBUG = False
