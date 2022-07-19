from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from projects.apps import ProjectsConfig
from projects.models import Project

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tags}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    context = {}
    return render(request, "projects/project_form.html", context)
