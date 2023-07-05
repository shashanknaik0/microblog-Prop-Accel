from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import PostSerializer
from .models import Post

# Create your views here.
@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def getUpdateOrDeletePost(request, post_id):
    return Response()
        

@api_view(['GET','POST'])
def getAllAndCreatePost(request):
    if request.method == 'GET':
        post = Post.objects.all()
        #serialize django query object
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)