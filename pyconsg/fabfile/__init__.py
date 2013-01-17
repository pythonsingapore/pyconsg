# flake8: noqa
from pyconsg import settings
from django.core.management import setup_environ
setup_environ(settings)


from development_fabfile.fabfile import *
from .local import *
