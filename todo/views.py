from django.shortcuts import render, HttpResponse
from .models import Todo

def pomepage(request):
    return render(request, 'index.html')
    
def test(request):
    Todo_list=Todo.objects.all()
    return render(request, 'test.html', {"Todo_list":Todo_list})
