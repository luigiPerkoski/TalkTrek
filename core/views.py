from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

import json

# Create your views here.
@api_view(['GET'])
def GetUsers(request):

    if request.method ==   'GET':

        users = CoreUser.objects.all()

        serializers = CoreUserSerializer(users, many= True)
        return Response(serializers.data)
    
    return Response(status= status.HTTP_400_BAD_REQUEST)



