from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from blog.forms import BlogPostForm
from blog.models import BlogPost
from common.mixins import TitleMixin


class BlogPostCreateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('main:home_page')
    title = 'Создание поста'
    permission_required = 'blog.add_blogpost'

    def form_valid(self, form):
        """
        Привязывает пост к текущему пользователю.
        """
        post = form.save()
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)


class BlogPostUpdateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    title = 'Редактирование поста'
    permission_required = 'blog.change_blogpost'

    def get_success_url(self):
        """
        Возвращает URL, на который должен быть перенаправлен пользователь после успешной обработки формы.
        """
        post = self.get_object()
        return reverse_lazy('blog:view_post', args=[post.pk])


class BlogPostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('main:home_page')
    permission_required = 'blog.delete_blogpost'


class BlogPostDetailView(TitleMixin, DetailView):
    model = BlogPost

    def get_title(self):
        """
        Возвращает заголовок страницы.
        """
        return self.object.title

    def get_object(self, queryset=None):
        """
        Увеличивает количество просмотров поста.
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
