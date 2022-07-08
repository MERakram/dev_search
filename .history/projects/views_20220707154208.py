from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def projects(request):
    return HttpResponse("here we are Projects")


def project(request, pk):
    return HttpResponse("here we are Project with id: " + str(pk))
