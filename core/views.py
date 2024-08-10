from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *




@api_view(['GET', 'POST'])
def users(request):


    if request.method == 'GET':

        users = CoreUser.objects.all()                          
        serializer = CoreUserSerializer(users, many=True)       

        return Response(serializer.data)                    




    if request.method == 'POST':

        new_user = request.data
        
        serializer = CoreUserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            user = CoreUser.objects.all()
            serializer = CoreUserSerializer(user, many=True)      
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    



    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def users_by_id(request, id):


    try:
        user = CoreUser.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)




    if request.method == 'GET':

        serializer = CoreUserSerializer(user)
        return Response(serializer.data)




    if request.method == 'PUT':

        serializer = CoreUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




    if request.method == 'DELETE':

        try:
            user.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        



    return Response(status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET', 'POST'])
def rooms(request):
    

    if request.method == 'GET':

        room = Room.objects.all()                      

        serializer = RoomSerializer(room, many=True)     

        return Response(serializer.data)                    




    if request.method == 'POST':

        new_room = request.data
        
        serializer = RoomSerializer(data=new_room)

        if serializer.is_valid():
            serializer.save()
            room = Room.objects.all()
            serializer = RoomSerializer(room, many=True)      
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    



    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def rooms_by_id(request, id):


    try:
        room = Room.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)




    if request.method == 'GET':

        serializer = RoomSerializer(room)
        return Response(serializer.data)




    if request.method == 'PUT':

        serializer = RoomSerializer(room, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




    if request.method == 'DELETE':

        try:
            room.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    



    return Response(status=status.HTTP_400_BAD_REQUEST)
