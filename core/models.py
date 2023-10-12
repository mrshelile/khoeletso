from django.db import models
from django.contrib.auth.models import AbstractUser
# class 
    
class User(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    location= models.CharField(max_length=50)
    location_geo=  models.JSONField(null=True,default=dict,)
    def __str__(self):
        return self.username
    
class Farmer(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
   
    def __str__(self):
        return self.id_number
    
    class Meta:
        verbose_name_plural = "Farmers"




# Create your models here.
