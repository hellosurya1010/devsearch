import profile
from django.shortcuts import render
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