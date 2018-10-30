from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True,null= False)
    full_name = models.CharField(max_length=100,null= False)
    email = models.EmailField(max_length=100,unique=True,null= False)
    password = models.CharField(max_length=20,null= False)
    conform_password = models.CharField(max_length=20,null=True)

