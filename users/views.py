import secrets

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.shortcuts import HttpResponseRedirect, render

from config.settings import DOMAIN_NAME, EMAIL_HOST_USER
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


class UserResetPassword(TitleMixin, TemplateView):
    title = 'Восстановление пароля'
    template_name = 'users/pwd_reset.html'
    success_url = 'users/'

    def post(self, request):
        """
        Обрабатывает запрос на восстановление пароля.
        """
        if self.request.method == 'POST':
            email = self.request.POST.get('email')
            try:
                user = User.objects.get(email=email)
                token = secrets.token_hex(10)
                link = f'{DOMAIN_NAME}/users'
                if User.objects.filter(email=email).exists():
                    subject = f'Восстановление пароля'
                    message = (f'Для восстановления доступа к личному кабинет пройдите по ссылке: {link} '
                               f'и воспользуйтесь временным паролем:\n {token}')
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email],
                        fail_silently=False,
                    )
                    user.password = make_password(token, salt=None, hasher='default')
                    user.save()
            except User.DoesNotExist:
                return HttpResponse(f'Пользователь с электронной почтой {email} не найден.')
        return render(request, self.template_name)
