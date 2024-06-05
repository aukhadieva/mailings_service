import smtplib

from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from datetime import datetime, timedelta
import pytz

from config import settings
from mailing.models import Mailing, MailingLog, LOGS_STATUS_CHOICES


def send_mailing():
    """Функция по отправке рассылки."""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = Mailing.objects.filter(created_datetime__lte=current_datetime).filter(status__in=['created', 'launched'])

    for mailing in mailings:

        title = mailing.message.title
        body = mailing.message.body

        mailing.status = 'launched'
        mailing.save()

        try:
            server_response = send_mail(
                subject=title,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.target.all()],
                fail_silently=False,
            )

            if server_response == 1:
                success_msg = 'письмо отправлено'
                MailingLog.objects.create(status=LOGS_STATUS_CHOICES[0][1], server_response=success_msg, mailing_id=mailing)

                if mailing.period == 'once':
                    mailing.created_datetime = current_datetime
                    mailing.status = 'completed'

                elif mailing.period == 'daily':
                    current_datetime = Mailing.objects.get(period='daily')
                    mailing.created_datetime = current_datetime.created_datetime + timedelta(days=1)

                elif mailing.period == 'weekly':
                    current_datetime = Mailing.objects.get(period='weekly')
                    mailing.created_datetime = current_datetime.created_datetime + timedelta(days=7)

                elif mailing.period == 'monthly':
                    current_datetime = Mailing.objects.get(period='monthly')
                    mailing.created_datetime = current_datetime.created_datetime + relativedelta(months=1)

                mailing.save()

        except smtplib.SMTPException as error:
            MailingLog.objects.create(status=LOGS_STATUS_CHOICES[1][1], server_response=error, mailing_id=mailing)
