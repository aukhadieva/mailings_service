from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.forms import ClientForm
from mailing.models import Client
from utils import TitleMixin


class ClientCreateView(TitleMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:index')
    title = 'Создание клиента'


class ClientListView(TitleMixin, ListView):
    model = Client
