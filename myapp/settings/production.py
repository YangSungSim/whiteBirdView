import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ[MYSQL_ROOT_HOST],
        'PORT': os.environ[MYSQL_ROOT_POST],
        'NAME': os.environ[MYSQL_DATABASE],
        'USER': os.environ[MYSQL_USER],
        'PASSWORD': os.environ[MYSQL_ROOT_PASSWORD],
    }
}