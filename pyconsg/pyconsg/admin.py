"""Extra admins for third party apps."""
from django.contrib import admin

from account.models import EmailAddress


class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'verified', 'primary', ]
    list_filter = ['verified', 'primary', ]
    search_fields = [
        'user__email', 'user__first_name', 'user__last_name', 'email', ]
    raw_id_fields = ['user', ]


admin.site.register(EmailAddress, EmailAddressAdmin)
