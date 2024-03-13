from django.shortcuts import render
from django.urls import reverse
from .models import User
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,GroupSerializer,changePasswordSerializer,EmailSerialzier,PasswordResetSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework import status
from django.contrib.auth import authenticate
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from EcommerceAPI import settings
import random
import datetime
from .tasks import email_verify_otp
# Create your views here.

#New registration function
class Registration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self,request):     
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        group_id= request.data.get('group')
        group_obj = Group.objects.filter(id=group_id).first()
        hash_password = make_password(password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if group_obj:
                user = User.objects.create(username=username,email=email,password=hash_password)
                user.groups.add(group_obj)
                user.save()
                user_data = {'user':username,'email':email}
                email_verify_otp.delay(user_data)
                return Response({'message':'User registration successfull'},status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Group does not exit'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)
    

#User login function      
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


# Owner Create fuction
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

# Group list ceck function
@api_view(['GET']) 
def GroupList(request):
    group_obj = Group.objects.all().exclude(name='Owner')
    serializer = GroupSerializer(group_obj,many=True)
    return Response(serializer.data)

# Change Password function
class ChangePasswordView(ModelViewSet):
    """
    An endpoint for changing password.
    """
    serializer_class = changePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(old_password):
                return Response({'error': 'Old password does not match'}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(new_password)
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Forgot password reset function
class PasswordResetView(ModelViewSet):
    serializer_class = EmailSerialzier
    permission_classes = [AllowAny]

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
                token = PasswordResetTokenGenerator().make_token(user)
                # Url: localhost:8000//reset-password/<encoded_pk>/<token>/
                reset_url = reverse(
                    "password-reset",
                    kwargs = {'encoded_pk':encoded_pk,'token':token}
                )
                reset_url = f"localhost:8000{reset_url}"
                return Response({'message': f"Your password reset link is {reset_url}"})
            else:
                return Response({'error': 'User does not exists'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)
        
class PasswordResetConfirm(ModelViewSet):
    serializer_class = PasswordResetSerializer

    def partial_update(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'kwargs':kwargs})
        if serializer.is_valid():
            return Response({'message': 'Your password reset complete'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)