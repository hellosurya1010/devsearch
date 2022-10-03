from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request, 'users/show.html')

def index(request):
    return render(request, 'users/index.html')