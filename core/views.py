from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

import json



@api_view(['GET'])
def GetUsers(request):

    if request.method == 'GET':

        users = CoreUser.objects.all()

        serializers = CoreUserSerializer(users, many= True)
        return Response(serializers.data)
    
    return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetUsersById(request, id):
    try:
        user = CoreUser.objects.get(pk=id)
    except CoreUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CoreUserSerializer(user)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

