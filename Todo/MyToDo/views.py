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

    
# When you need to access multiple fields of each Todo object, we use:
# todos = Todo.objects.all()
# for todo in todos:
#     print(todo.id, todo.title, todo.details)  # Access all fields

# When we want to retrieve only the specific field of Todo object or When you only need specific fields (like IDs) and not the full model instances.we use:
#     or
    
# When you want a more efficient query that uses less memory, especially if you have a lot of fields in your model but only need a few of them.
    
#     todo_ids = Todo.objects.values_list('id',flat=True) #Gets a list of ids
#     print(todo_ids)