from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ReviewForm

projectlist = [
    {'id': 1, 'name': 'ehealth', 'description': 'Medical app'},
    {'id': 2, 'name': 'ndgeme', 'description': 'Financial app'},
    {'id': 3, 'name': 'letters pack', 'description': 'Chatting app'},
]


def projects(request):
    projects = Project.objects.all()
    page = request.GET['page']
    results = 3
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except EmptyPage:
        page = Paginator.num_pages
    except PageNotAnInteger:
        page = Paginator.num_pages
    projects = paginator.page(page)
    return render(request, 'projects/index.html', {'projects': projects, 'paginator': paginator})


def project(request, id):
    project = Project.objects.get(id=id)
    form = ReviewForm()
    print(project.id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user.profile
            form.project = project
            form.save()
            project.calculateVoteRatio
            return redirect('project', id=id)
    tags = project.tags.all()
    return render(request, 'projects/show.html', {'project': project, 'tags': tags, 'form': form})


@login_required(login_url='login')
def createProject(request):
    forms = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('projects')
    context = {'forms': forms}
    return render(request, 'projects/create.html', context)


@login_required(login_url='login')
def updateProject(request, id):
    project = Project.objects.get(id=id)
    if project.owner_id == request.user.profile.id:
        forms = ProjectForm(instance=project)
        if request.method == "POST":
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('projects')
        context = {'forms': forms}
        return render(request, 'projects/update.html', context)
    else:
        messages.warning(request, 'Your dont have access to edit')
        return redirect('users.account')

@login_required(login_url='login')
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('projects') 
