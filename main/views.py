from django.views.generic import TemplateView

from blog.models import BlogPost
from mailing.models import Mailing, Client
from utils import TitleMixin


class MainTemplateView(TitleMixin, TemplateView):
    title = 'Главная'
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        """
        Возвращает данные контекста для отображения списка объектов.
        """
        context_data = super().get_context_data(**kwargs)
        context_data['posts'] = BlogPost.objects.all()
        context_data['mailings'] = Mailing.objects.all()
        context_data['clients'] = Client.objects.all()
        return context_data
