from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from management.models import EmployeeInfo
from management.serializers import EmployeeInfoSerializer


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
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_owner(request):
    email = request.data.get('email')
    password = request.data.get('password')
    serializer = UserSerializer(data=request.data)
    group = Group.objects.get(name='owner')
    if serializer.is_valid():
        hash_password = make_password(password)
        user_obj = User.objects.create(email=email,password=hash_password)
        user_obj.groups.add(group)
        return Response('User Created')
    else:
        return Response(serializer.errors)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def employeeInfoView(request):
    name = request.data.get('name')
    number = request.data.get('number')
    email = request.data.get('email')
    password = request.data.get('password')
    serializer = EmployeeInfoSerializer(data=request.data)
    if serializer.is_valid():
        hash_password = make_password(password)
        emp_info = EmployeeInfo.objects.create(name=name,number=number,email=email,password=hash_password)
        emp_info.save()
        user_obj = User.objects.create(email=email,password=hash_password)
        user_obj.save()
        return Response('Employee Info saved & Employee User Login Id created')
    else:
        return Response(serializer.errors)
    


    





