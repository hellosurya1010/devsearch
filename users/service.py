from users.models import Profile, Skill
from .forms import ProfileForm, SkillForm
from django.shortcuts import HttpResponse, render, redirect


class Get:

    def accontEditForm(request):
        user = request.user.profile
        form = ProfileForm(instance=user)
        context = {'user': user, 'form': form}
        return render(request, 'users/edit-account.html', context)

    def skill(request):
        form = SkillForm()
        context = {'form': form}
        return render(request, 'users/skill-form.html', context)

    def skillUpdate(request, id):
        profile = request.user.profile
        skill = profile.skill_set.get(id=id)
        form = SkillForm(instance=skill)
        context = {'form': form}
        return render(request, 'users/skill-form.html', context)

    def skillDelete(request, id):
        profile = request.user.profile
        skill = profile.skill_set.get(id=id)
        skill.delete()
        return redirect('users.account')

class Post:

    def accontEditForm(request):
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('users.account')

    def skill(request):
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            profile = request.user.profile
            skill.owner = profile
            skill.save()
        return redirect('users.account')


    def skillUpdate(request, id):
        profile = request.user.profile
        skill = profile.skill_set.get(id=id)
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
        return redirect('users.account')
