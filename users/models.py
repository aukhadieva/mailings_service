from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    image = models.ImageField(upload_to='users_images/', blank=True, null=True, verbose_name='аватар')
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class EmailVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='пользователь')
    key = models.UUIDField(unique=True, verbose_name='ключ')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата генерации ключа')
    expiration = models.DateTimeField(verbose_name='срок действия ключа')

    def __str__(self):
        return f'подтверждение электронной почты для {self.user}'

    class Meta:
        verbose_name = 'подтверждение электронной почты'
