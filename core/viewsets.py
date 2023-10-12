from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response  # Import Response class
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    # authentication_classes = [TokenAuthentication]  # Use TokenAuthentication for authentication

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the request data
        
        mutable_data = request.data.copy()

        # Hash the password using make_password
        # if 'password' in mutable_data:
        #     mutable_data['password'] = make_password(mutable_data['password'])

        # Serialize the mutable data using the serializer
        # print(mutable_data)
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)

        # Return a response with the serialized data and token
        response_data = {
            'user': serializer.data,
            'token': token.key  # Include the token key in the response
        }
        # Return a success response with the serialized data
        return Response(response_data, status=201)

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
