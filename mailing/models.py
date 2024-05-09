from django.db import models


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
