from django.urls import path

from users.apps import UsersConfig
from users.views import sign_in, sign_up, profile, logout

app_name = UsersConfig.name

urlpatterns = [
    path('signin/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')
]
