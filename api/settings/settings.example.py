from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your Key here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR DB NAME HERE',
        'USER': 'YOUR UN HERE',
        'PASSWORD': 'YOUR PW HERE'
        'HOST': 'db',
        'PORT': '3306',
    }
}
