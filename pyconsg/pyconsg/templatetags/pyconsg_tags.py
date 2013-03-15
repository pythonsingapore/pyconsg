"""Templatetags for the ``pyconsg`` project."""
from django import template

from cmsplugin_blog.models import Entry
from symposion.speakers.models import Speaker


register = template.Library()


@register.assignment_tag
def get_latest_blog_entries(amount=5):
    return Entry.objects.all().published()[:amount]


@register.assignment_tag
def get_speaker(name):
    """Returns a speaker object selected by the given name."""
    return Speaker.objects.get(name=name)
