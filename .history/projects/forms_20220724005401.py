import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image',
                  'description', 'tags', 'vote_ratio']
