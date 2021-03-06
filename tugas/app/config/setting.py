import os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'g=hy28h&on^w=42&y8a7qzs6+bxs*-*w+4sb!joxtbh4qo^b6x'
DEBUG = True
ALLOWED_HOSTS = [

]

PROJECT_APPS = [
    'anggota',

]

REQUIRED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = REQUIRED_APPS + PROJECT_APPS

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'


from app.config.auth import *
from app.config.database import *
from app.config.timeutc import *
from app.config.static import *
django.setup()
from app.config.template import *