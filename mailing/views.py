from django.urls import reverse_lazy
from django.views.generic import CreateView

from mailing.forms import ClientForm
from mailing.models import Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:index')
