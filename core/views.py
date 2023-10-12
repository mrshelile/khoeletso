from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import *
from .serializers import UserSerializer
import json

@csrf_exempt  # Add this decorator to disable CSRF protection for this view
def custom_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username'  ]
        password = data['password']
       
        # password = make_password(password)
        # print(password)
        # print(username)
        # user = authenticate(username=username, password=password)
        try:
            user = User.objects.get(username=username,password=password)
        except:
            user=None
        # print(user.password)
        # user=None
        if user:
            # User is authenticated, generate a token
            token = user.auth_token.key
            return JsonResponse({'token': token,"user":UserSerializer(user).data})
        else:
            # Invalid credentials
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Create your views here.
