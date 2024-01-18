from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Bill,Payment
from rest_framework.response import Response
from .serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
from core.permissions import CustomPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# # Create your views here.
# @api_view(['GET'])
# def bill_view(request):
#     bill_obj = Bill.objects.all()
#     bill_json = BillSerializer(bill_obj,many=True)
#     return Response(bill_json.data)

class BillView(ModelViewSet):
    # Method 1 
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [CustomPermissions]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['guest']
    search_fields = ['amount']

    # Inheritance method 2
    def list(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset,many=True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
              return Response('Data Not found!')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    def update(self,request,pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
              return Response('Data Not found!')
        serializer = self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
    def destroy(self,request,pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
            queryset.delete()
            return Response('Data delete')
        except:
              return Response('Data Not found!')
        