from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import PostSerializer
from .models import Post

# Create your views here.
@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def getUpdateOrDeletePost(request, post_id):
    post=None

    try:
        post = Post.objects.get(id = post_id)
    except Exception:
        return Response("Post with id "+str(post_id)+" does not exist", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        #serialize django query object
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']: 
        #updating fields
        #since it is illogical to update userid, i am not allowing to update userid
        #if we want to update user id,then get the object of user model with specified id and asign to post.user_id
        post.content = request.data['content']

        #saving to database
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response("Post with id "+str(post_id)+" is deleted")
                
@api_view(['GET','POST'])
def getAllAndCreatePost(request):
    if request.method == 'GET':
        post = Post.objects.all()
        #serialize django query object
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        #validate as specified in model
        if serializer.is_valid():
            #saving to database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)