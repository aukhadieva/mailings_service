from django.core.cache import cache

from blog.models import BlogPost
from config.settings import CACHE_ENABLED


def get_posts_from_cache():
    """
    Получает данные по постам из кэша,
    если кэш пуст - получает данные из БД.
    """
    if not CACHE_ENABLED:
        return BlogPost.objects.filter(is_published=True)[:4]
    key = 'post_list'
    posts = cache.get(key)
    if posts is not None:
        return posts
    posts = BlogPost.objects.filter(is_published=True)[:4]
    cache.set(key, posts)
    return posts
