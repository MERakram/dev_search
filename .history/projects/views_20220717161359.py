from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from projects.apps import ProjectsConfig
from projects.models import Project

# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': ' Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'This was a project where I built out my portfol',
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description':  'Awesome open source project I am still working',
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)
