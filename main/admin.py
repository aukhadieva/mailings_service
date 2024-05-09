from django.contrib import admin

from mailing.models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email',)
    search_fields = ('full_name',)
