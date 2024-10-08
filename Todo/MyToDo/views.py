from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo


# Create your views here.


def add_item(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Details submitted successfully')
    form = TodoForm()
    page = {
        "todo_form":form,
        "list":item_list,
        "title":"TODO LIST"
    }
    
    return render(request,"MyToDo/index.html",page)


  ####################give id no. item_id name or item_id=i.id ############
### function to remove item, it receive todo item_id as primary key from url ##

def remove_item(request,item_id):
    print("Received request to remove item with ID:", item_id)
    print("Current Todo IDs:", Todo.objects.values_list('id', flat=True))  # Log current IDs
    if request.method == "POST":
        item = get_object_or_404(Todo,id=item_id)  # Automatically handles DoesNotExist
        item.delete()
        messages.info(request, "Item removed!")
    else:
        messages.error(request, "Invalid request method.")
    return redirect("todo:add")
    



