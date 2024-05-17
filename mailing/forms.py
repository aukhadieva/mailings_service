from django import forms

from mailing.models import Client, MailingMessage, Mailing


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
