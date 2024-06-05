from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create_post', BlogPostCreateView.as_view(), name='create_post'),
    path('edit_post/<int:pk>', BlogPostUpdateView.as_view(), name='edit_post'),
    path('view_post/<int:pk>', cache_page(60)(BlogPostDetailView.as_view()), name='view_post'),
    path('delete_post/<int:pk>', BlogPostDeleteView.as_view(), name='delete_post'),
]
