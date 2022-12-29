from django import template
from ..models import Menu
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(name=menu_name)

    html = '\n'.join([m.render(context['request']) for m in menu])
    html = (
        '<ul style="list-style-type: circle; padding: 0; margin: 10px;"'
        + html
        + '</ul>'
    )
    html = mark_safe(html)

    return html
