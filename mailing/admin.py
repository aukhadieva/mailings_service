from django.contrib import admin

from mailing.models import Client, MailingMessage, Mailing


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email',)
    search_fields = ('full_name',)


@admin.register(MailingMessage)
class AdminMailingMessage(admin.ModelAdmin):
    list_display = ('id', 'title', 'body',)
    search_fields = ('title', 'body',)


@admin.register(Mailing)
class AdminMailing(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'period', 'status', 'owner',)
    search_fields = ('title',)
    list_filter = ('created_datetime', 'period', 'status', 'owner',)
