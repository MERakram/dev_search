from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse("here we are Projects")


def project(request, pk):
    return HttpResponse("here we are Project with id: " + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
]
