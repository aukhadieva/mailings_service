from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.forms import ClientForm, MailingMessageForm, MailingForm, ModeratorMailingForm
from mailing.models import Client, MailingMessage, Mailing, MailingLog
from utils import TitleMixin


class ClientCreateView(TitleMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    title = 'Создание клиента'
    permission_required = 'mailing.add_client'


class ClientListView(TitleMixin, LoginRequiredMixin, ListView):
    model = Client
    title = 'Список клиентов'


class ClientDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    model = Client

    def get_title(self):
        return self.object.full_name


class ClientDeleteView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    title = 'Удаление клиента'
    permission_required = 'mailing.delete_client'


class ClientUpdateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    title = 'Редактирование клиента'
    permission_required = 'mailing.edit_client'

    def get_success_url(self):
        client = self.get_object()
        return reverse('mailing:view_client', args=[client.pk])


class MailingMessageCreateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:message_list')
    title = 'Создание сообщения'
    permission_required = 'mailing.add_mailingmessage'


class MailingMessageListView(TitleMixin, LoginRequiredMixin, ListView):
    model = MailingMessage
    title = 'Список сообщений'
    login_url = reverse_lazy('users:login')


class MailingMessageDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    model = MailingMessage
    login_url = reverse_lazy('users:login')

    def get_title(self):
        return self.object.title


class MailingMessageUpdateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    title = 'Редактирование сообщения'
    permission_required = 'mailing.edit_mailingmessage'

    def get_success_url(self):
        message = self.get_object()
        return reverse('mailing:view_message', args=[message.pk])


class MailingMessageDeleteView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:message_list')
    title = 'Удаление сообщения'
    permission_required = 'mailing.delete_mailingmessage'


class MailingCreateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    title = 'Создание рассылки'
    permission_required = 'mailing.add_mailing'


class MailingListView(TitleMixin, LoginRequiredMixin, ListView):
    model = Mailing
    title = 'Список рассылок'


class MailingDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    model = Mailing

    def get_title(self):
        return self.object.title


class MailingUpdateView(TitleMixin, LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    title = 'Редактирование рассылки'

    def get_success_url(self):
        mailing = self.get_object()
        return reverse('mailing:view_mailing', args=[mailing.pk])

    def get_form_class(self):
        """
        Возвращает форму исходя из прав пользователя.
        """
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingForm
        if user.has_perm('mailing.change_mailing_status'):
            return ModeratorMailingForm
        raise PermissionDenied


class MailingDeleteView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
    title = 'Удаление рассылки'
    permission_required = 'mailing.delete_mailing'


class MailingLogListView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MailingLog
    title = 'Логи рассылки'
    permission_required = 'mailing.view_mailinglog'


class MailingLogDetailView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = MailingLog
    title = 'Логи рассылки'
    permission_required = 'mailing.view_mailinglog'
