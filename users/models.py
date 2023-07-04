from django.db import models

# Create your models here.
class User(models.Model):
    #model fields
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True,null=False)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=20,null=False)