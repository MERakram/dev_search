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
    context = {'projects': projectsList, 'page' = page}
    msg = 'fuck you now and forever'
    return render(request, 'projects/projects.html', {'message': msg})


def project(request, pk):
    return render(request, 'projects/single-project.html')
