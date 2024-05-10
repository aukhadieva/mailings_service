from django import forms

from mailing.models import Client, MailingMessage


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
