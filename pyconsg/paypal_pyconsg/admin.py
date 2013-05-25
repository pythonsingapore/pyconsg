"""Admin classes for the ``paypal_pyconsg`` app."""
from django.contrib import admin

from .models import CheckoutChoices


class CheckoutChoicesAdmin(admin.ModelAdmin):
    model = CheckoutChoices
    list_display = [
        'user', 'user__email', 'transaction', 'is_student',
        'has_conference_ticket', 'tutorial_morning', 'tutorial_afternoon',
        'tshirt_size', ]
    search_fields = [
        'user__email', 'user__first_name', 'user__last_name',
        'transaction__transaction_id', ]

    def user__email(self, obj):
        return obj.user.email


admin.site.register(CheckoutChoices, CheckoutChoicesAdmin)
