from .models import User
from rest_framework import serializers,status
from django.contrib.auth.models import Group
from django.contrib.auth import password_validation

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

class changePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['old_password','new_password','confirm_password']
        '''
        serializer password change endpoint
        '''
    old_password = serializers.CharField(max_length=250,write_only=True,required=True)
    new_password = serializers.CharField(max_length=250,write_only=True,required=True)
    confirm_password = serializers.CharField(max_length=250,write_only=True,required=True)

    def validate(sefl,data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'error': 'Two password fields does not match'})
        
        password = data['confirm_password']
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