from django import forms

from mailing.models import Client, MailingMessage, Mailing
from common.mixins import StyleMixin


class ClientForm(StyleMixin, forms.ModelForm):
    """
    Форма подписки по email.
    """

    class Meta:
        model = Client
        fields = ('full_name', 'email', 'comment',)


class MailingMessageForm(StyleMixin, forms.ModelForm):
    """
    Форма сообщения для рассылки.
    """

    class Meta:
        model = MailingMessage
        fields = ('title', 'body',)


class MailingForm(StyleMixin, forms.ModelForm):
    """
    Форма для рассылки.
    """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['target'].queryset = Client.objects.filter(owner=user)
        self.fields['message'].queryset = MailingMessage.objects.filter(owner=user)

    class Meta:
        model = Mailing
        fields = ('title', 'period', 'status', 'target', 'message',)


class ModeratorMailingForm(StyleMixin, forms.ModelForm):
    """
    Форма для модератора рассылки.
    """

    class Meta:
        model = Mailing
        fields = ('status',)
