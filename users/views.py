from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import UserSerializer
from .models import User

# Create your views here.
@api_view(['GET','PUT','PATCH'])
def getOrUpdateUser(request, user_id):
    if request.method == 'GET':
        user=None
        try:
            user = User.objects.get(id = user_id)
        except Exception:
            return Response("User with id "+str(user_id)+" does not exist", status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method in ['PUT','PATCH']:
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                 
                user=None
                try:
                    user = User.objects.get(id = user_id)
                except Exception:
                    return Response("User with id "+str(user_id)+" does not exist", status=status.HTTP_400_BAD_REQUEST)
                user.username = serializer.data['username']
                user.email = serializer.data['email']
                user.password = serializer.data['password']
                user.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)