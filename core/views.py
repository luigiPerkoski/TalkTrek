from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

import json



@api_view(['GET','POST','PUT','DELETE'])
def UsersView(request, id = None):

    if id:


        try:
            user = CoreUser.objects.get(pk=id)
        except CoreUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
            serializer = CoreUserSerializer(user)
            return Response(serializer.data)
        

        if request.method == 'PUT': #TODO: Create put method for put the user by ID
            ...
        

        if request.method == 'DELETE': #TODO: Create delete method for delete the user by ID
            ...



        return Response(status=status.HTTP_400_BAD_REQUEST)
    




    if request.method == 'GET':

        users = CoreUser.objects.all()

        serializers = CoreUserSerializer(users, many= True)
        return Response(serializers.data)
    


    if request.method == 'POST': #TODO: Resolver esse pepino depois 
        
        new_user = request.data
    
        serializer = CoreUserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



    return Response(status= status.HTTP_400_BAD_REQUEST)
        


