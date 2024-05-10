from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.forms import ClientForm, MailingMessageForm, MailingForm
from mailing.models import Client, MailingMessage, Mailing
from utils import TitleMixin


class ClientCreateView(TitleMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    title = 'Создание клиента'


class ClientListView(TitleMixin, ListView):
    model = Client
    title = 'Список клиентов'


class ClientDetailView(TitleMixin, DetailView):
    model = Client

    def get_title(self):
        return self.object.full_name


class ClientDeleteView(TitleMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    title = 'Удаление клиента'


class ClientUpdateView(TitleMixin, UpdateView):
    model = Client
    form_class = ClientForm
    title = 'Редактирование клиента'

    def get_success_url(self):
        client = self.get_object()
        return reverse('mailing:view_client', args=[client.pk])


class MailingMessageCreateView(TitleMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:message_list')
    title = 'Создание сообщения'


class MailingMessageListView(TitleMixin, ListView):
    model = MailingMessage
    title = 'Список сообщений'


class MailingMessageDetailView(TitleMixin, DetailView):
    model = MailingMessage

    def get_title(self):
        return self.object.title


class MailingMessageUpdateView(TitleMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    title = 'Редактирование сообщения'

    def get_success_url(self):
        message = self.get_object()
        return reverse('mailing:view_message', args=[message.pk])


class MailingMessageDeleteView(TitleMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:message_list')
    title = 'Удаление сообщения'


class MailingCreateView(TitleMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    title = 'Создание рассылки'


class MailingListView(TitleMixin, ListView):
    model = Mailing
    title = 'Список рассылок'


class MailingDetailView(TitleMixin, DetailView):
    model = Mailing

    def get_title(self):
        return self.object.title


class MailingUpdateView(TitleMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    title = 'Редактирование рассылки'

    def get_success_url(self):
        mailing = self.get_object()
        return reverse('mailing:view_mailing', args=[mailing.pk])


class MailingDeleteView(TitleMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
    title = 'Удаление рассылки'
