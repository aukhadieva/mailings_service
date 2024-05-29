import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now

from users.models import User, EmailVerification
from utils import StyleMixin


class UserLoginForm(StyleMixin, AuthenticationForm):
    """
    Форма для авторизации и аутентификации пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password',)


class UserRegistrationForm(StyleMixin, UserCreationForm):
    """
    Форма для регистрации пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=True)
        key = uuid.uuid4()
        expiration = now() + timedelta(hours=24)
        verification = EmailVerification.objects.create(user=user, key=key, expiration=expiration)
        verification.send_verification_email()
        return user


class UserProfileForm(StyleMixin, UserChangeForm):
    """
    Форма для профиля пользователя.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'email',)
