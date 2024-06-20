import os 
from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['kapa.liara.run']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}