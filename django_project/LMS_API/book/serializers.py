from rest_framework import serializers
from .models import Book
from rest_framework import status

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['author']:
            for name in data['author']:
                if name.isdigit():
                    raise serializers.ValidationError(status=status.HTTP_400_BAD_REQUEST)
        return data