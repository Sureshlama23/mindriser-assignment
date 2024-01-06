from dataclasses import field
from rest_framework import serializers
from .models import Bill,Payment

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields ='__all__'
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
