from multiprocessing import context
from multiprocessing.dummy import current_process
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

projectlist = [
    {'id': 1, 'name': 'ehealth', 'description': 'Medical app'},
    {'id': 2, 'name': 'ndgeme', 'description': 'Financial app'},
    {'id': 3, 'name': 'letters pack', 'description': 'Chatting app'},
]

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def project(request, id):
    project = Project.objects.get(id=id)
    tags = project.tags.all()
    return render(request, 'projects/show.html', {'project': project, 'tags': tags })

def createProject(request):
    forms = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'forms': forms}
    return render(request, 'projects/create.html', context)

def updateProject(request, id):
    project = Project.objects.get(id=id)
    forms = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'forms': forms}
    return render(request, 'projects/show.html', context)

def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects') 
