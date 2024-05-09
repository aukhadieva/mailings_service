from django import forms

from mailing.models import Client


class ClientForm(forms.ModelForm):
    """
    Форма подписки по email.
    """
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'ФИО'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Комментарий'}))

    class Meta:
        model = Client
        fields = ('full_name', 'email', 'comment',)
