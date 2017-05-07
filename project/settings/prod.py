from project.settings.base import *

DEBUG = False
# TODO: DRY in fabric files
ALLOWED_HOSTS = ['smolinska.eu', 'www.smolinska.eu']
GOOGLE_ANALYTICS_ID = ''
INSTALLED_APPS.remove('django_gulp')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}


# COMPRESS_OFFLINE = True
