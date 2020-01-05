from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoitem



# Create your views here.

def mytaskview(request):
    #return HttpResponse('<h1>My to-do List</h1>')
    all_item = todoitem.objects.all()  
    return render(request,'todo.html' , {'all':all_item})


def updateview(request):  
    return render(request,'update.html')

def addtask(request):
    write= request.POST['contents']
    new_todo= todoitem(contents=write)
    new_todo.save()   
    return HttpResponseRedirect('/')

def deletetask(request, todo_id):
    
    task_to_delete= todoitem.objects.get(id= todo_id)    
    task_to_delete.delete()   
    return HttpResponseRedirect('/')

def edittask(request, edit_id):
    
    task_to_edit= todoitem.objects.get(id= edit_id)
    task_to_edit.contents= request.POST.get('contents')
    task_to_edit.save()
    return HttpResponseRedirect('/')

def addtodopage(request):
    return render(request,'add.html')

def deletetodopage(request):
    all_item = todoitem.objects.all()
    return render(request,'delete.html', {'all':all_item})

def edittodopage(request):
    all_item = todoitem.objects.all()
    return render(request,'edit.html', {'all':all_item})

