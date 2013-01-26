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
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
]

EXTERNAL_APPS = [
    'south',

    # theme
    # 'pinax_theme_bootstrap_account',
    # 'pinax_theme_bootstrap',
    'django_forms_bootstrap',
    'theme_orcur',

    # external
    'admin_honeypot',
    'debug_toolbar',
    'mailer',
    'timezones',
    'metron',
    'markitup',
    'taggit',
    'reversion',
    'easy_thumbnails',
    'sitetree',
    'account',

    # symposion
    'symposion',
    'symposion.sponsorship',
    'symposion.conference',
    'symposion.cms',
    'symposion.boxes',
    'symposion.proposals',
    'symposion.speakers',
    'symposion.teams',
    'symposion.reviews',
    'symposion.schedule',
]

# We are splitting up the INSTALLED_APPS setting because this is helpful when
# running tests and creating coverage output only for our own internal apps.
INTERNAL_APPS = [
    'pyconsg',
    'proposals_pyconsg',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from pyconsg.settings.installed_apps.mailer import *  # NOQA
from pyconsg.settings.installed_apps.debug_toolbar import *  # NOQA
from pyconsg.settings.installed_apps.account import *  # NOQA
from pyconsg.settings.installed_apps.markitup import *  # NOQA
from pyconsg.settings.installed_apps.symposion import *  # NOQA
