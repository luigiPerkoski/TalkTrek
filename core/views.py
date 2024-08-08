from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *



@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

    if request.GET['id']:

        if request.method == 'GET':

            try:                        
                id = request.GET['id']         

                try:
                    user = CoreUser.objects.get(pk=id)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = CoreUserSerializer(user)           
                return Response(serializer.data)            
                
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)




        if request.method == 'PUT':

            id = request.data['id']

            try:
                updated_user = CoreUser.objects.get(pk=id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            
            serializer = CoreUserSerializer(updated_user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)




        if request.method == 'DELETE':

            try:
                user_to_delete = CoreUser.objects.get(pk=request.data['id'])
                user_to_delete.delete()
                return Response(status=status.HTTP_202_ACCEPTED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            

    else:
        

        if request.method == 'GET':

            users = CoreUser.objects.all()
            serializers = CoreUserSerializer(users, many= True)

            return Response(serializers.data)




        if request.method == 'POST':

            new_user = request.data
            
            serializer = CoreUserSerializer(data=new_user)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            return Response(status=status.HTTP_400_BAD_REQUEST)
