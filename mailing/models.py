from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента, получающего рассылки."""
    full_name = models.CharField(max_length=500, verbose_name='Ф.И.О.')
    email = models.EmailField(verbose_name='контактный email')
    comment = models.CharField(max_length=500, verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingMessage(models.Model):
    """Модель письма в рассылке."""
    title = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):
    """Модель рассылки."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='менеджер рассылки')
    title = models.CharField(max_length=300, verbose_name='название рассылки')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время первой отправки рассылки')
    period = models.CharField(max_length=50, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=50, verbose_name='статус рассылки')
    target = models.ManyToManyField(Client, verbose_name='получатели рассылки')
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='сообщение рассылки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
