"""Context processors for the ``theme_orcur`` app."""
from django.conf import settings


def theme(request):
    ctx = {
        'ANALYTICS_TRACKING_ID': getattr(
            settings, 'ANALYTICS_TRACKING_ID', ''),
    }
    return ctx
