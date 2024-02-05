from django.shortcuts import render
from .models import MenuItem


def mainmenu(request):
    menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu/mainmenu.html', {'menu_items': menu_items})


def selected_item(request, item_name):
    menu_items = MenuItem.objects.filter(name=item_name)
    return render(request, 'menu/selected_item.html', {'item_name': item_name})
