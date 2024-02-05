from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # - параметр <item_name> передаётся в функцию и в ней обрабатывается
    #   это сделано для избавления от избыточности в файлах и загромождения кода.
    path('<item_name>/', views.selected_item, name="selected_item"),

]
