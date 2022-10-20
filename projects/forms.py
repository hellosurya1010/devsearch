from dataclasses import field
from tkinter import Widget
from django.forms import ModelForm
from .models import Project, Review
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link',
                  'source_link', 'tags', 'featured_image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter project title',
        })

        self.fields['demo_link'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter project demo link',
        })

        self.fields['source_link'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter project source link',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter project description',
            'style': 'height: 80px',
        })


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']
        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
