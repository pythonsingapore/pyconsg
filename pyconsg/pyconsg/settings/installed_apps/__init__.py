"""Installed apps for the pyconsg project."""

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.markup',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
]

EXTERNAL_APPS = [
    # globally needed
    'south',
    'admin_honeypot',
    'debug_toolbar',
    'mailer',

    # theme
    # 'pinax_theme_bootstrap_account',
    # 'pinax_theme_bootstrap',
    'django_forms_bootstrap',
    'theme_orcur',

    # django-filer related
    'filer',
    'easy_thumbnails',

    # external symposion related
    'timezones',
    'metron',
    'markitup',
    'taggit',
    'account',

    # symposion
    'symposion',
    'symposion.sponsorship',
    'symposion.conference',
    'symposion.boxes',
    'symposion.proposals',
    'symposion.speakers',
    'symposion.teams',
    'symposion.reviews',
    'symposion.schedule',

    # django-cms
    'cms',
    'menus',
    'mptt',
    'sekizai',
    'cmsplugin_blog',
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'missing',
    'cmsplugin_markdown',
]

# We are splitting up the INSTALLED_APPS setting because this is helpful when
# running tests and creating coverage output only for our own internal apps.
INTERNAL_APPS = [
    'pyconsg',
    'proposals_pyconsg',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from .account import *  # NOQA
from .cms import *  # NOQA
from .debug_toolbar import *  # NOQA
from .mailer import *  # NOQA
from .markitup import *  # NOQA
from .symposion import *  # NOQA
