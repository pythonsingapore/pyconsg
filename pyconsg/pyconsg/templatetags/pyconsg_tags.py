"""Templatetags for the ``pyconsg`` project."""
from django import template

from cmsplugin_blog.models import Entry


register = template.Library()


@register.assignment_tag
def get_latest_blog_entries(amount=5):
    return Entry.objects.all().published()[:amount]
