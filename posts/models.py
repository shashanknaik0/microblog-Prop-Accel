from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(to=User,on_delete=models.CASCADE)
    content = models.CharField(max_length=255,null=False)
    post_date = models.DateTimeField(auto_now_add=True)