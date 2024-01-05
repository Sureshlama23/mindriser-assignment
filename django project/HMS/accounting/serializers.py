from dataclasses import field
from rest_framework import serializers
from .models import Bill,Payment

class BillSerializer(serializers.Serializer):
    class Meta:
        model = Bill
        field ='__all__'
    
class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        field = '__all__'
