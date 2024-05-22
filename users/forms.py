from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User
from utils import StyleMixin


class UserLoginForm(StyleMixin, AuthenticationForm):
    """
    Форма для авторизации и аутентификации пользователя.
    """

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(StyleMixin, UserCreationForm):
    """
    Форма для регистрации пользователя.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class UserProfileForm(StyleMixin, UserChangeForm):
    """
    Форма для профиля пользователя.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email',)
