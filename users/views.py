from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET','PUT','PATCH'])
def getOrUpdateUser(request, user_id):
    user=None
    try:
        user = User.objects.get(id = user_id)
    except Exception:
        return Response("User with id "+str(user_id)+" does not exist", status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        #serialize django query object
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
        #we can check here if we want only logged in user want to update (by using req.user.is_authenticated)

        #updating fields
        user.username = request.data['username']
        user.email = request.data['email']
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.set_password(request.data['password'])
        #saving to database
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        

@api_view(['POST'])
def postUser(request):
    #serialize data as specified in user model
    serializer = UserSerializer(data=request.data)
    #validate as specified in model
    if serializer.is_valid():
        #saving to database
        serializer.create(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)