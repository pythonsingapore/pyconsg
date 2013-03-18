"""ProposalBase implementations for the PyCon SG project."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import ProposalBase


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^timezones\.fields\.TimeZoneField"])


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3
    AUDIENCE_LEVEL_ALL = 4

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, 'Novice'),
        (AUDIENCE_LEVEL_INTERMEDIATE, 'Intermediate'),
        (AUDIENCE_LEVEL_EXPERIENCED, 'Experienced'),
        (AUDIENCE_LEVEL_ALL, 'All'),
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text=(
            'By submitting your talk proposal, you agree to give permission to'
            ' the conference organizers to record, edit, and release audio'
            ' and/or video of your presentation. If you do not agree to this,'
            ' please uncheck this box.')
    )

    class Meta:
        abstract = True


class TalkProposal(Proposal):
    class Meta:
        verbose_name = 'talk proposal'


class TutorialProposal(Proposal):
    class Meta:
        verbose_name = 'tutorial proposal'


class StartupBoothProposal(Proposal):
    class Meta:
        verbose_name = 'startup booth proposal'

    AGE_CHOICES = [
        ('0-3', _('0 - 3 months')),
        ('4-6', _('4 - 6 months')),
        ('7-9', _('7 - 9 months')),
        ('10-12', _('10 - 12 months')),
        ('12+', _('Over a year')),
    ]

    startup_url = models.URLField(
        verbose_name=_('What is the URL of your startup?'),
    )

    startup_age = models.CharField(
        max_length=16,
        choices=AGE_CHOICES,
        verbose_name=_('How old is your startup?'),
    )

    is_launched = models.BooleanField(
        default=False,
        verbose_name=_('Have you launched?'),
    )
