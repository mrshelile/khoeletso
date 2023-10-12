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
    # product = models.OneToOneField("core.Product",null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_number
    
    class Meta:
        verbose_name_plural = "Farmers"

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # owner= models.OneToOneField(Farmer, on_delete=models.)
    owner = models.ForeignKey(Farmer,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField(default=0)  # Default value is 0
    image=models.ImageField( upload_to="images/",null=True)
    rate = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    

    # quantity - 






# Create your models here.
