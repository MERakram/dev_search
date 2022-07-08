from email import message
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def projects(request):
    msg = 'fuck you now and forever'
    return render(request, 'projects/projects.html', message=msg)


def project(request, pk):
    return render(request, 'projects/single-project.html')
