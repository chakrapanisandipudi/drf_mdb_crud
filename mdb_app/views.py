from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from mdb_app.models import Tutorials
from mdb_app.serializers import TutorialSerializer
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def tutoriallist(request):
    """
    Get a Tutorials list, Update Tutorials List and Delete all tutorials
    """
    if request.method == 'GET':
        tutorials = Tutorials.objects.all()

        title = request.GET.get('title', None)
        if title is  not None:
            tutorials = tutorials.filter(title__iscontains=title)
        
        tutorial_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data, safe=False)
    
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        count = Tutorials.objects.all().delete()
        return JsonResponse({'message': '{} tutorials were deleted succesfully...'.format([0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    """
    Get a Tutorials list using ID
    """   
    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)
    
    elif request.method == 'PUT':
        tutorial_data = JsonResponse().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        else:
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        tutorial = Tutorials.objects.get(pk=pk)
    except Tutorials.DoesNotExist:
        raise JsonResponse({'message': 'the tutorial not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tutorial_list_published(request):
    """
    Get a Tutorials list, Update Tutorials List and Delete all tutorials
    """
    tutorials = Tutorials.objects.filter(published=True)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data, safe=False)