from django.db import models

from users.models import User


class BlogPost(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='контент-менеджер')
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', blank=True, null=True)
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
