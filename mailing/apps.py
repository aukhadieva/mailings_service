from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    # def ready(self):
    #     """
    #     Настройки конфигурации для периодического запуска задачи по отправке рассылок.
    #     """
    #     from mailing.cron import send_mailing
    #     sleep(2)
    #     send_mailing()
