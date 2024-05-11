from django import forms

from mailing.models import Client, MailingMessage, Mailing, MAILING_STATUS_CHOICES, PERIOD_CHOICES
from users.models import User


class ClientForm(forms.ModelForm):
    """
    Форма подписки по email.
    """
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'ФИО'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Комментарий'}), required=False)

    class Meta:
        model = Client
        fields = ('full_name', 'email', 'comment',)


class MailingMessageForm(forms.ModelForm):
    """
    Форма сообщения для рассылки.
    """
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Тема письма'}))
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-5', 'placeholder': 'Тело письма'}))

    class Meta:
        model = MailingMessage
        fields = ('title', 'body',)


class MailingForm(forms.ModelForm):
    """
    Форма для рассылки.
    """
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    owner = forms.ModelChoiceField(queryset=User.objects.all())
    period = forms.CharField(widget=forms.Select(choices=PERIOD_CHOICES))
    status = forms.CharField(widget=forms.Select(choices=MAILING_STATUS_CHOICES))
    target = forms.ModelMultipleChoiceField(queryset=Client.objects.all())
    message = forms.ModelChoiceField(queryset=MailingMessage.objects.all())

    class Meta:
        model = Mailing
        fields = ('title', 'owner', 'period', 'status', 'target', 'message',)
