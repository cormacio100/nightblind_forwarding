from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')   #   CLEARDB_DATABASE_URL retrieved from Heroku App
}

SITE_URL = 'https://nightblind.herokuapp.com'
ALLOWED_HOSTS.append('nightblind.herokuapp.com')


# Log DEBUG information to the console
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
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}