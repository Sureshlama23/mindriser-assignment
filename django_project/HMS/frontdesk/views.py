from django.shortcuts import render
from rest_framework.response import Response
from .serializers import GuestInfoSerializer,GuestRoomSerializer
from .models import GuestRoom,GuestInfo
from rest_framework.viewsets import ModelViewSet
from core.permissions import CustomPermissions
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter,OrderingFilter



# Create your views here.
class GuestInfoView(ModelViewSet):
    queryset = GuestInfo.objects.all()
    serializer_class = GuestInfoSerializer
    permission_classes = [CustomPermissions]
    filter_backends = [ SearchFilter]
    search_fields = ['name','Phone_no']
    def lit(self, request):
        guest_obj = self.get_queryset()
        filter_queryset = self.filter_queryset(guest_obj)
        serializer = self.serializer_class(filter_queryset,many=True)
        return Response({"status": 200, "payload": serializer.data})
    
    def create(self, request):
        serializer = GuestInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Guest info saved"})
        else:
            return Response({"status": 403, "error": serializer.errors})
    
    def retrieve(self, request,pk):
        try:
            queryset = GuestInfo.objects.get(id=pk)
            serializer = self.serializer_class(queryset)
            return Response({"status": 200, "payload": serializer.data})
        except:
              return Response('Data Not found!')
    def update(self, request,pk):
        guestinfo_obj = GuestInfo.objects.get(id=pk)
        serializer = GuestInfoSerializer(guestinfo_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "guestinfo update success"})
        else:
            return Response({"status": 403, "error": serializer.errors})
    
    def destroy(self,request,pk):
        try:
            guestinfo_obj = GuestInfo.objects.get(id=pk)
            guestinfo_obj.delete()
            return Response({"status": 200, "message": "Data delete success"})
        except:
            return Response({"status": 403, "error": "Data not found"})
        
    

