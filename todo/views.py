from django.shortcuts import render, HttpResponse, redirect
from .models import Todo

def pomepage(request):
    return render(request, 'index.html')
    
def test(request):
    Todo_list=Todo.objects.all()
    return render(request, 'test.html', {"Todo_list":Todo_list})

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=Todo(text=text)
    todo.save()
    return redirect(test)
