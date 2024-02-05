from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/list_items.html")
def draw_menu(menu_name=None):
    if menu_name == "main_menu":
        menu_items = MenuItem.objects.all()
    else:
        menu_items = MenuItem.objects.filter(name=menu_name)
    return {"menu_items": menu_items}
