from django.core.management.base import BaseCommand

from mailing.cron import send_mailing


class Command(BaseCommand):
    """Команда для отправки рассылки."""
    def handle(self, *args, **options):
        send_mailing()
