"""Installed apps for the pyconsg project."""

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
]

EXTERNAL_APPS = []

# We are splitting up the INSTALLED_APPS setting because this is helpful when
# running tests and creating coverage output only for our own internal apps.
INTERNAL_APPS = [
    'pyconsg',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
