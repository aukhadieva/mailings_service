# Generated by Django 5.0.5 on 2024-05-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='контактный email'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='period',
            field=models.CharField(choices=[('once', 'один раз'), ('daily', 'ежедневно'), ('weekly', 'еженедельно'), ('monthly', 'ежемесячно')], default='', max_length=50, verbose_name='периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('completed', 'завершена'), ('launched', 'запущена')], default='created', max_length=50, verbose_name='статус рассылки'),
        ),
    ]
