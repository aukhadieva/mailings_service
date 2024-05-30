from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.shortcuts import HttpResponseRedirect

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification
from common.mixins import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Авторизация'


class UserRegisterView(TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
    title = 'Регистрация'


class UserProfileView(LoginRequiredMixin, TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_object(self, queryset=None):
        """
        Метод для получения объекта пользователя.
        Переопределяется, чтобы не передавать pk текущего пользователя.
        """
        return self.request.user


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает запрос на подтверждение электронной почты.
        """
        key = kwargs['key']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, key=key)
        group = Group.objects.get(name='Mailing owner')
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_active = True
            user.groups.add(group)
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('main:index'))
