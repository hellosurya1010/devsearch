from ast import Try
import profile
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .models import Post as Po
from .service import Get, Post

# Create your views here.

def show(request, id):
    profile = Profile.objects.get(id=id)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile": profile, "topSkills": topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/show.html', context)

def index(request):
    profiles = Profile.objects.all()
    print(profiles)
    context = {'profiles': profiles}
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

@login_required(login_url='login')
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

def search(request, searchfor):
    profiles = Profile.objects.filter(name__icontains=request.GET['value'])
    context = { "profiles": profiles }
    return render(request, 'ajax/porfile-search.html', context)
