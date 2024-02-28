from django.shortcuts import render
from .models import User
from django.contrib.auth.models import Group
from .serializers import UserSerializer,GroupSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.
class Registration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self,request):
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            group_id= request.data.get('group')
            group_obj = Group.objects.get(id=group_id)
            hash_password = make_password(password)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.create(username=username,email=email,password=hash_password)
                user.groups.add(group_obj)
                user.save()
                return Response({'message':'User registration successfull'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        except:
            return Response({"error": "Value missing"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
@api_view(['POST'])
@permission_classes([AllowAny])       
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email,password=password)
    if user is not None:
        return Response({"message": "User login successfully"},status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)

        
class OwnerCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def create(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        group_obj = Group.objects.get(name='Owner')
        hash_password = make_password(password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(username=username,email=email,password=hash_password,is_staff=True)
            user.groups.add(group_obj)
            user.save()
            return Response({'message':'Owner user registration successfull'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

@api_view(['GET']) 
def GroupList(request):
    group_obj = Group.objects.all().exclude(name='Owner')
    serializer = GroupSerializer(group_obj,many=True)
    return Response(serializer.data)