from blog.settings.base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogger',
        'USER': 'Database_User', 
        'PASSWORD': 'Database_User_Password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = BASE_DIR / "static/"