from django.db import models

# Create your models here.
class Info(models.Model):
    Id = models.AutoField(primary_key=True,unique = True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=100)
    
    

    