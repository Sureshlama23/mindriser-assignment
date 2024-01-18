from dataclasses import field
from rest_framework import serializers
from accounting.models import Bill,Payment
from frontdesk.serializers import GuestInfoSerializer

class BillSerializer(serializers.ModelSerializer):
    guest = GuestInfoSerializer()
    class Meta:
        model = Bill
        fields ='__all__'
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
