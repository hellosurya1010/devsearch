from ast import Try
from contextlib import redirect_stderr
import imp
import profile
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm, MessageForm, ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Message, Profile, Skill
from .models import Post as Po
from .service import Get, Post
from projects.models import Project, Tag

# Create your views here.

def show(request, id):
    profile = Profile.objects.get(id=id)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile": profile, "topSkills": topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/show.html', context)

def index(request):
    profiles = Profile.objects.all()
    page = 1
    if request.GET:
        page = request.GET['page']
    result = 4
    paginator = Paginator(profiles, result)
    try:
        profiles = paginator.page(page)
    except EmptyPage:
        page = Paginator.num_pages
    except PageNotAnInteger:
        page = Paginator.num_pages
    profiles = paginator.page(page)
    context = {'profiles': profiles, 'paginator': paginator}
    return render(request, 'users/index.html', context)

def registerUser(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User account is created')
            return redirect('users.index')

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context) 

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('users.index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')
        user = authenticate(request, )
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome "+username)
            return redirect('users.index')
        else:
            messages.error(request, 'username or password is in correct')

    return render(request, 'users/login.html') 

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def account(request):
    user = User.objects.all()
    print(user)
    profile = request.user.profile
    skills = profile.skill_set.all()
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def accountEdit(request):
    if request.method == "GET":
        return Get.accontEditForm(request)    
    if request.method == "POST":
        return Post.accontEditForm(request)

@login_required(login_url="login")        
def skill(request):
    if request.method == "GET":
        return Get.skill(request)    
    if request.method == "POST":
        return Post.skill(request)
        
@login_required(login_url='login')
def skillUpdate(request, id):
    if request.method == "GET":
        return Get.skillUpdate(request, id)
    if request.method == "POST":
        return Post.skillUpdate(request, id)
        
@login_required(login_url='login')
def skillDelete(request, id):
        return Get.skillDelete(request, id)

def query(request):
    posts = Po.objects.get(title="django")
    posts.title = 'Laravel'
    posts.description = 'Laravel is an MVC framework'
    posts.save()
    return HttpResponse(posts)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messagesModel = profile.messages.all()
    noOfUnreadedMessages = messagesModel.filter(is_readed=False).count()
    context = {'messagesModel': messagesModel, "noOfUnreadedMessages": noOfUnreadedMessages}
    return render(request, 'messages/inbox.html', context)


def search(request, searchfor):
    if searchfor == 'users':
        search = request.GET['value']
        skills =  Skill.objects.filter(name__iexact=search)
        tags = Tag.objects.filter(name__icontains=search)
        profiles = Profile.objects.distinct().filter(
            Q(name__icontains=search) | Q(bio__icontains=search) | Q(skill__in=skills)
            )  
        projects = Project.objects.filter(Q(title__contains=search) | Q(tags__in=tags))
        context = { "profiles": profiles, "skills": skills, "projects": projects }
        return render(request, 'ajax/porfile-search.html', context)
    return HttpResponse('No response')

@login_required(login_url='login')
def message(request, id):
    profile = request.user.profile
    message = profile.messages.get(id=id)
    if message.is_readed == False:
        message.is_readed = True
        message.save()
    context = {'message': message}
    return render(request, 'messages/message.html', context)


def sendMessage(request, id):
    profile = Profile.objects.get(id=id)
    messageForm = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.sender = request.user.profile
            form.receiver = profile
            form.save()
            messages.success(request, 'Message has send successfully')
            return redirect('users.show', id=id)
    context = {"profile": profile, "messageForm": messageForm}
    return render(request, 'messages/message.html', context)