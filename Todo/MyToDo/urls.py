from django.contrib import admin
from django.urls import path

from . views import index,remove


app_name = "todo"

urlpatterns = [
    path("",index,name="todo"),
    path("del/<str:item_id>",remove,name="delete"),
    path("admin/",admin.site.urls)
       
]
