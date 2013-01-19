from django.contrib import admin

from proposals_pyconsg.models import (
    TalkProposal,
    TutorialProposal,
    StartupBoothProposal,
)


admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
admin.site.register(StartupBoothProposal)
