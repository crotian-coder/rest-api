from django.shortcuts import render
from api.serializers import TaskSerializer
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from api import serializers



@api_view(['GET'])

def Home(request):

    return HttpResponse("<h1> go to /api </h1>")


@api_view(['GET'])

def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',

    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item deleted succsesfully')

    
