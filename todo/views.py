from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoitem



# Create your views here.

def mytaskview(request):
    #return HttpResponse('<h1>My to-do List</h1>')
    all_item = todoitem.objects.all()  
    return render(request,'todo.html' , {'all':all_item})

def addtask(request):
    write= request.POST['contents']
    new_todo= todoitem(contents=write)
    new_todo.save()
    
    return HttpResponseRedirect('/')

def deletetask(request, todo_id):
    task_to_delete= todoitem.objects.get(id= todo_id)
    
    task_to_delete.delete()
    
    return HttpResponseRedirect('/')
