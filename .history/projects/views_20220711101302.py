from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

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
    page = 'projects'
    context = {'projects': projectsList, 'page': page}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = None
    for i in projectsList:
        if i['id'] == pk:
            project_obj = i
    context = {'project': project_obj}
    # 'project': project_obj
    return render(request, 'projects/single-project.html', context)
