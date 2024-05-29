import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        superuser = User.objects.create(
            email='admin@bk.ru',
            first_name='admin',
            last_name='admin',
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        superuser.set_password(os.getenv('SU_PASSWORD'))
        superuser.save()
