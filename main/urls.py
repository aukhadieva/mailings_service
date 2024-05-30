from django.urls import path

from main.apps import MainConfig
from main.views import MainTemplateView

app_name = MainConfig.name

urlpatterns = [
    path('', MainTemplateView.as_view(), name='home_page')
]
