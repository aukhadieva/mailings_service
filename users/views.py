from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def sign_in(request):
    """
    Авторизация и аутентификация пользователя.
    """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/sign_in.html', context)


def sign_up(request):
    """
    Регистрация пользователя.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:sign_in'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/sign_up.html', context)
