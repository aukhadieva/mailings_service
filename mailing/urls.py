from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (ClientCreateView, ClientListView, ClientDetailView, ClientDeleteView, ClientUpdateView,
                           MailingMessageCreateView, MailingMessageListView, MailingMessageDetailView,
                           MailingMessageDeleteView, MailingMessageUpdateView,
                           MailingCreateView, MailingListView, MailingDetailView, MailingDeleteView, MailingUpdateView,
                           MailingLogListView, MailingLogDetailView)

app_name = MailingConfig.name

urlpatterns = [
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('view_client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('create_message', MailingMessageCreateView.as_view(), name='create_message'),
    path('message_list/', MailingMessageListView.as_view(), name='message_list'),
    path('view_message/<int:pk>', MailingMessageDetailView.as_view(), name='view_message'),
    path('delete_message/<int:pk>', MailingMessageDeleteView.as_view(), name='delete_message'),
    path('edit_message/<int:pk>', MailingMessageUpdateView.as_view(), name='edit_message'),
    path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('view_mailing/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='edit_mailing'),
    path('mailinglogs_list/', MailingLogListView.as_view(), name='mailinglogs_list'),
    path('view_mailinglog/<int:pk>', MailingLogDetailView.as_view(), name='view_mailinglog'),
]
