from django.shortcuts import render


def sign_in(request):
    return render(request, 'users/sign_in.html')


def sign_up(request):
    return render(request, 'users/sign_up.html')
