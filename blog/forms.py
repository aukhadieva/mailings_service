from django.forms import ModelForm

from blog.models import BlogPost
from common.mixins import StyleMixin


class BlogPostForm(StyleMixin, ModelForm):
    """
    Форма для создания и редактирования поста в блоге.
    """
    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'image')
