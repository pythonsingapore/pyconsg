"""
Forms for the ``paypal_express_checkout`` app in the ``pyconsg`` context.

"""
from django import forms
from django.utils.translation import ugettext_lazy as _

from paypal_express_checkout.models import Item
from paypal_express_checkout.forms import SetExpressCheckoutFormMixin


class PyconsgSetExpressCheckoutForm(SetExpressCheckoutFormMixin):
    conference_tickets = forms.IntegerField(
        min_value=0,
        label=_('Conference tickets'),
        initial=1,
        widget=forms.TextInput(
            attrs={'style': 'width: 2em; float: left; margin-right: 1em;', }),
    )

    student_tickets = forms.IntegerField(
        min_value=0,
        label=_('Conference tickets (Student rate)'),
        initial=0,
        widget=forms.TextInput(
            attrs={'style': 'width: 2em; float: left; margin-right: 1em;', }),
    )

    tutorial_tickets = forms.IntegerField(
        min_value=0,
        label=_('Tutorial tickets'),
        initial=0,
        widget=forms.TextInput(
            attrs={'style': 'width: 2em; float: left; margin-right: 1em;', }),
    )

    def __init__(self, *args, **kwargs):
        super(PyconsgSetExpressCheckoutForm, self).__init__(*args, **kwargs)
        self.conference_item = Item.objects.get(identifier='conference-early')
        self.student_item = Item.objects.get(identifier='conference-student')
        self.tutorial_item = Item.objects.get(identifier='tutorial')

    def clean(self):
        data = self.cleaned_data
        if (data.get('conference_tickets', 0) == 0
                and data.get('tutorial_tickets', 0) == 0
                and data.get('student_tickets', 0) == 0):
            raise forms.ValidationError(
                'You have to buy at least one ticket.')
        return data

    def get_items_and_quantities(self):
        """
        Returns the items and quantities.

        Should return a list of tuples.

        """
        data = self.cleaned_data
        result = []
        if data['conference_tickets'] > 0:
            result.append((self.conference_item, data['conference_tickets']))
        if data['student_tickets'] > 0:
            result.append((self.student_item, data['student_tickets']))
        if data['tutorial_tickets'] > 0:
            result.append((self.tutorial_item, data['tutorial_tickets']))
        return result
