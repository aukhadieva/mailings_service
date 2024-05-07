from django.urls import path

from users.apps import UsersConfig
from users.views import sign_in, sign_up

app_name = UsersConfig.name

urlpatterns = [
    path('signin/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
]
