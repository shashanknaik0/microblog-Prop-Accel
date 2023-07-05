from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET','PUT','PATCH'])
def getOrUpdateUser(request, user_id):
    if request.method == 'GET':
        user=None
        try:
            user = User.objects.get(id = user_id)
        except Exception:
            return Response("User with id "+str(user_id)+" does not exist", status=status.HTTP_400_BAD_REQUEST)
        #serialize django query object
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
            #serialize data as specified in user model
            serializer = UserSerializer(data=request.data)

            #validate as specified in model
            if serializer.is_valid():
                user=None
                try:
                    user = User.objects.get(id = user_id)
                except Exception:
                    return Response("User with id "+str(user_id)+" does not exist", status=status.HTTP_400_BAD_REQUEST)
                
                #updating fields
                user.username = serializer.data['username']
                user.email = serializer.data['email']
                user.password = serializer.data['password']
                user.first_name = serializer.data['first_name']
                user.last_name = serializer.data['last_name']
                #saving to database
                user.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def postUser(request):
    #serialize data as specified in user model
    serializer = UserSerializer(data=request.data)
    #validate as specified in model
    if serializer.is_valid():
        #saving to database
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)