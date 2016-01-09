from os.path import basename

from project.settings.base import *

DEBUG = False
host = 'alpakara.pl'
ALLOWED_HOSTS = [host, 'www.' + host]
GOOGLE_ANALYTICS_ID = ''

MEDIA_URL = 'http://{}/demo/{}/media/'.format(host, basename(BASE_DIR))

INSTALLED_APPS.remove('django_gulp')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
