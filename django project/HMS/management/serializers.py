from rest_framework import serializers
from .models import EmployeeInfo

class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'