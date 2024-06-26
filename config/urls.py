from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('main.urls', namespace='main')),
    path('mailing/', include('mailing.urls', namespace='mailing')),
    path('posts/', include('blog.urls', namespace='blog'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
