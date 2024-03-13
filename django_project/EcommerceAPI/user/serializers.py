from .models import User
from rest_framework import serializers,status
from django.contrib.auth.models import Group
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def validate(self,data):
        # Password Strength validation
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
        # Two password field match checking
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'error': 'Two password fields does not match'})
        
        # Password Strength validation
        password = data['confirm_password']
        if len(password) < 6:
            raise serializers.ValidationError({'error': 'Password length should be at least 6.'})
        
        if not any(p.isupper() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 upper letter.'})
            
        if not any(p.isdigit() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 digit.'})
        return data
    
class EmailSerialzier(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email']

class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['new_password','confirm_password']
    '''
        Serializer password reset end point
    '''
    new_password = serializers.CharField(max_length=250,write_only=True,required=True)
    confirm_password = serializers.CharField(max_length=250,write_only=True,required=True)

    def validate(self,data):
        # Two password field match checking
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'error': 'Two password fields does not match'})
        
        # Password Strength validation
        password = data['confirm_password']
        if len(password) < 6:
            raise serializers.ValidationError({'error': 'Password length should be at least 6.'})
        
        if not any(p.isupper() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 upper letter.'})
            
        if not any(p.isdigit() for p in password):
            raise serializers.ValidationError({'error': 'Password must contain at least 1 digit.'})
        
        # Token and encoded_pk validation
        token = self.context.get('kwargs').get('token')
        encoded_pk = self.context.get('kwargs').get('encoded_pk')
        if (token or encoded_pk) is None:
            raise serializers.ValidationError({'error': 'Missing value'})
        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user,token=token):
            raise serializers.ValidationError({'The reset token is invalid!'})
        user.set_password(password)
        user.save()
        return data
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']