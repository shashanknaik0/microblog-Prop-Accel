from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        #only these fields will be avilable in json response
        fields= ["id", "user_id", "post_date", "content"]