import os.path as op

BASE_DIR = op.abspath(op.join(__file__, '../../..'))

# Application definition
INSTALLED_APPS = [
    'django_gulp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'ordered_model',
    'ckeditor',
    'compressor',

    # required for gallery
    'django.contrib.sites',
    'photologue',
    'sortedm2m',

    # our stuff
    'apps.main',
]

# required for gallery { https://django-photologue.readthedocs.org/en/3.2/pages/installation.html }
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [op.join(BASE_DIR, 'project', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = op.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = op.join(BASE_DIR, 'static')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter', 'compressor.filters.jsmin.SlimItFilter']
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

SITE_URL = 'http://www.sliczna36.pl'  # DO NOT END IT WITH SLASH!

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': op.join(BASE_DIR, 'db.sqlite3'),
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ooba^l1%kv*^hx7a0dziwp0(+u2q%ul5fn&e@$f3wr2mj_hjh3'

from project.settings.project import *