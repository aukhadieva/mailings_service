from django import template

from mailing.forms import ClientForm

register = template.Library()


@register.inclusion_tag('mailing/client_form_tag.html')
def client_form():
    return {'client_form': ClientForm()}
