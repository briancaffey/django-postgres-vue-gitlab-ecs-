from .base import * # noqa

DEBUG_APPS = [
    'django_extensions',
    'debug_toolbar'
]


INSTALLED_APPS += DEBUG_APPS

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

log_level = "INFO"
if DEBUG:
    log_level = "DEBUG"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'portal': {
            'handlers': ['console'],
            'level': os.getenv('PORTAL_LOG_LEVEL', log_level),
        },
    },
}

EMAIL_USE_TLS = False


NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--allow-root',
    '--no-browser',
]

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'