from django.shortcuts import render
from .models import User
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer,GroupSerializer,changePasswordSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password,check_password
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

class PasswordReset(ModelViewSet):
    pass

# Change Password
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