from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', ClientCreateView.as_view(), name='create_client'),
]
