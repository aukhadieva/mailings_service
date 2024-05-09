from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientCreateView, ClientListView, ClientDetailView

app_name = MailingConfig.name

urlpatterns = [
    path('', ClientCreateView.as_view(), name='create_client'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('view_client/<int:pk>', ClientDetailView.as_view(), name='view_client')
]
