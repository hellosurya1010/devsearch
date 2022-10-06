from ast import Try
import profile
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

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
