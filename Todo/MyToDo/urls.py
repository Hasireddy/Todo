from django.contrib import admin
from django.urls import path

from . views import add_item,remove_item


app_name = "todo"

urlpatterns = [
    path("",add_item,name="add"),
    path("delete/<int:item_id>/",remove_item,name="delete"),
       
]
