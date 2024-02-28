from rest_framework import serializers
from .models import shopDetail

class shopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = shopDetail
        fields = '__all__'
