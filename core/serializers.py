# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = FarmerSerializer(many=False,required=False)
    #  owner= serializers.PrimaryKeyRelatedField(queryset= User.objects.all(),)
    class Meta:
        model = Product
        fields = ['id','url','created','owner','name','description','price','image','rate','quantity'] 

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'