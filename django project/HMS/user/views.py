from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user != None:
        token, _ =  Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        return('Invalid credentials!')