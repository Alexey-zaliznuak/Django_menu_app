from django.template import Library, loader, Template
from ..models import Menu
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(name=menu_name)
    html = '\n'.join([m.render(context['request']) for m in menu])
    return loader.render_to_string('draw_menu_container.html', {'html':html})
