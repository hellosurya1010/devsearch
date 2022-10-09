from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": 'form-control'})    

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'location', 'email', 'job', 'short_intro', 'bio', 'profile_image', 'social_linkedin', 'social_github', 'social_youtube', 'social_twitter'] 

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if name == 'bio':
                field.widget.attrs.update({'style': 'height: 60px'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'style': 'min-height: 15px !important'})