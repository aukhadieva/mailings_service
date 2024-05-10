from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (ClientCreateView, ClientListView, ClientDetailView, ClientDeleteView, ClientUpdateView,
                           MailingMessageCreateView, MailingMessageListView, MailingMessageDetailView,
                           MailingMessageDeleteView, MailingMessageUpdateView)

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
]
