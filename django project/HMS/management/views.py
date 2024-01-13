from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import EmployeeInfo
from .serializers import EmployeeInfoSerializer
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from user.serializers import UserSerializer
from user.models import User
from rest_framework.response import Response

# Create your views here.
class EmployeeInfoView(ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeInfoSerializer

    def create(self,request):
       email = request.data.get('email')
       password = request.data.get('password')
       group_id = request.data.get('group')
       group_obj = Group.objects.get(id=group_id)
       hash_password = make_password(password)
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer = self.serializer_class(data=request.data)
           if serializer.is_valid():
               user = User.objects.create(email=email,password=hash_password)
               user.groups.add(group_obj) 
               obj = serializer.save()
               obj.user = user
               obj.save()
               return Response(serializer.data)
           else:
               return Response(serializer.errors)
       else:
           return Response(serializer.errors)