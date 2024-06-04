from django.views.generic import TemplateView

from blog.models import BlogPost
from common.mixins import TitleMixin
from mailing.models import Mailing, Client


class MainTemplateView(TitleMixin, TemplateView):
    title = 'Главная'
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        """
        Возвращает данные контекста для отображения списка объектов.
        """
        context_data = super().get_context_data(**kwargs)

        context_data['posts'] = BlogPost.objects.filter(is_published=True)[:4]

        mailings = Mailing.objects.all()
        context_data['mailings'] = len(mailings)

        active_mailings = Mailing.objects.filter(status='launched')
        context_data['active_mailings'] = len(active_mailings)

        clients = Client.objects.all()
        context_data['clients'] = len(clients)
        return context_data
