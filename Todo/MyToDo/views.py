from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo


# Create your views here.


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Details submitted successfully')
    form = TodoForm()
    page = {
        "forms":form,
        "list":item_list,
        "title":"TODO LIST"
    }
    
    return render(request,"MyToDo/index.html",page)



### function to remove item, it receive todo item_id as primary key from url ##

def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"Item removed !!!")
    return redirect("todo")



