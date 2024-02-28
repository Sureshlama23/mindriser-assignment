from .models import User
from rest_framework import serializers,status
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self,data):
        password = data['password']
        if len(password) < 6:
            raise serializers.ValidationError({'error': 'Password length should be at least 6.'})
        
        if not any(p.isupper() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 upper letter.'})
            
        if not any(p.isdigit() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 digit.'})
        return data
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']