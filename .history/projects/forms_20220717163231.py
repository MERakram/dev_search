import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        field = '__all__'
