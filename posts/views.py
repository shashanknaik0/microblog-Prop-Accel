from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def getUpdateOrDeletePost(request, post_id):
    return Response()
        

@api_view(['POST'])
def createPost(request):
    return Response()