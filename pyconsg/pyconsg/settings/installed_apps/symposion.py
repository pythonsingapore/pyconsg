"""Settings for the ``symposion`` app."""

CONFERENCE_ID = 1

SYMPOSION_PAGE_REGEX = r'(([\w-]{1,})(/[\w-]{1,})*)/'

PROPOSAL_FORMS = {
    'tutorial': 'symposion_project.proposals.forms.TutorialProposalForm',
    'talk': 'symposion_project.proposals.forms.TalkProposalForm',
    'poster': 'symposion_project.proposals.forms.PosterProposalForm',
}
