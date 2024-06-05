from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from config.settings import DOMAIN_NAME, EMAIL_HOST_USER


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

    class Meta:
        permissions = [
            ('change_is_active_status', 'Can change user`s status'),
        ]


class EmailVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='пользователь')
    key = models.UUIDField(unique=True, verbose_name='ключ')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата генерации ключа')
    expiration = models.DateTimeField(verbose_name='срок действия ключа')

    def __str__(self):
        return f'подтверждение электронной почты для {self.user}'

    class Meta:
        verbose_name = 'подтверждение электронной почты'

    def send_verification_email(self):
        """
        Отправляет электронное письмо с ключом подтверждения эл. почты.
        """
        link = reverse('users:verify', kwargs={'email': self.user.email, 'key': self.key})
        verification_link = f'{DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи'
        message = f'Для подтверждения регистрации пройдите по ссылке:\n {verification_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        """
        Проверяет, истек ли срок действия ключа.
        """
        return True if now() >= self.expiration else False
