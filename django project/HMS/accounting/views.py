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
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    