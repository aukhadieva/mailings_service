from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User
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
