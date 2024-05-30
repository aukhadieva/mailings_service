from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class AdminBlogPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'views_count',)
    list_filter = ('is_published', 'created_at',)
    search_fields = ('title', 'body',)
