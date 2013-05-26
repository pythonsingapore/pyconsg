"""Templatetags for the ``pyconsg`` project."""
from django import template

from cmsplugin_blog.models import Entry
from symposion.schedule.models import Room, Presentation
from symposion.speakers.models import Speaker


register = template.Library()


@register.assignment_tag
def get_latest_blog_entries(amount=5):
    return Entry.objects.all().published()[:amount]


@register.assignment_tag
def get_rooms():
    return Room.objects.all()


@register.assignment_tag
def get_speaker(name):
    """Returns a speaker object selected by the given name."""
    return Speaker.objects.get(name=name)


@register.assignment_tag
def get_speakers():
    """Returns all speakers with accepted proposals."""
    speakers = Speaker.objects.filter(presentations__isnull=False).distinct()
    return speakers


@register.assignment_tag
def get_startups():
    """Returns all accepted startups."""
    startups = Presentation.objects.filter(
        proposal_base__kind__slug='startupbooth').order_by('title')
    return startups
