from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True,null=False)
    email = models.CharField(max_length=50,unique=True,null=False)
    password = models.CharField(max_length=20,null=False)