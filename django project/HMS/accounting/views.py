from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Bill,Payment
from rest_framework.response import Response
from .serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet


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
    # Inheritance method 2
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
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
            queryset = Bill.objects.get(id=Pk)
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
        except:
              return Response('Data Not found!')
        queryset.delete()
        return Response('Data delete')