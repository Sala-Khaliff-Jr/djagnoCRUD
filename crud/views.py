from django.shortcuts import render
from django.db.models.query import EmptyQuerySet
from .models import Todo
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'crud/index.html')
    
def create(request):
    if request.method == "POST":
        todo = request.POST.get('todo')
        Todo.objects.create(task_desc = todo)
        return render(request,'crud/create.html',{'flag':'True'})
    else:
        return render(request,'crud/create.html')

def read(request,task_id,action):
    if(request.method == "POST"):
        if(action == 'update'):
            new_task = request.POST.get('todo')
            print(new_task)
            print("task ID" ,task_id)
            # Todo.objects.get(id = task_id)
            obj = Todo.objects.get(id = task_id)
            obj.task_desc = new_task
            obj.save()
        if(action == 'delete'):
            obj = Todo.objects.get(id = task_id)
            obj.delete()
            todo_items = Todo.objects.all()
            flag = isinstance(Todo.objects.none(), EmptyQuerySet)
            print("this is todo items",flag)
            if (flag != True):
                todo_items['todo_items'] = 'None'

            return render(request,'crud/read.html',{'todo_items':todo_items})
        
    # print("read success",request.POST.get(id = task_id))
    if(action == 'create'):
            return render(request,'crud/create.html',{'flag':'True'})
    todo_items = Todo.objects.all()
    # if Todo.objects.count() == 0:
    #     todo_items = 0
    # print("items are being printed right",todo_items)
    return render(request,'crud/read.html',{'todo_items':todo_items})  

def update(request,id=0,link=''):
    print(link)
    print("Id is received",id)
    item = Todo.objects.get(id=id)
    return render(request,"crud/update.html",{'item':item,'id':id})    

# def update(request,link):
#     return redirect('edit')
    # print("Id is received",id)
    # item = Todo.objects.get(id=id)
    # return render(request,"crud/update.html",{'item':item})              