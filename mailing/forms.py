from django import forms

from mailing.models import Client, MailingMessage, Mailing
from utils import StyleMixin


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

    class Meta:
        model = Mailing
        fields = ('title', 'owner', 'period', 'status', 'target', 'message',)


class ModeratorMailingForm(StyleMixin, forms.ModelForm):
    """
    Форма для модератора рассылки.
    """

    class Meta:
        model = Mailing
        fields = ('status',)
