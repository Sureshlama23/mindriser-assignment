from rest_framework import serializers
from .models import GuestInfo,GuestRoom
from management.serializers import RoomSerializer

class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestInfo 
        fields = '__all__'

    def validate(self, data):
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"status": 403, "error": "Name must be alphabet!"})
        if data['Phone_no']:
            str_data = str(data['Phone_no'])
            if len(str_data) < 10:
                raise serializers.ValidationError({"status": 403, "error": "Nunber should be 10 digit!"})
                
        return data

class GuestRoomSerializer(serializers.ModelSerializer):
    guest = GuestInfoSerializer()
    room  = RoomSerializer()
    class Meta:
        model = GuestRoom
        fields = '__all__'