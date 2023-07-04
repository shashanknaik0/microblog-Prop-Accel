from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def getUser(request, user_id):
    user = User.objects.get(id = user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)