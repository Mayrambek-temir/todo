from django.shortcuts import render, HttpResponse

def pomepage(request):
    return render(request, 'index.html')
