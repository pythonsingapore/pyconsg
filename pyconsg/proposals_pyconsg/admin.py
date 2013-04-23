from django.contrib import admin

from proposals_pyconsg.models import (
    TalkProposal,
    TutorialProposal,
    StartupBoothProposal,
)


class TalkProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'submitted']


class TutorialProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'submitted']


class StarupBoothProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'submitted']


admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(TutorialProposal, TutorialProposalAdmin)
admin.site.register(StartupBoothProposal, StarupBoothProposalAdmin)
