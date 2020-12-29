from django.db import models

# Create your models here.
class User_Data(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    
