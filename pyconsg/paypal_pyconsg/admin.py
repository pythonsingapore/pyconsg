"""Admin classes for the ``paypal_pyconsg`` app."""
from django.contrib import admin

from .models import CheckoutChoices


class CheckoutChoicesAdmin(admin.ModelAdmin):
    model = CheckoutChoices
    list_display = [
        'user', 'transaction', 'is_student', 'has_conference_ticket',
        'tutorial_morning', 'tutorial_afternoon', 'tshirt_size', ]


admin.site.register(CheckoutChoices, CheckoutChoicesAdmin)
