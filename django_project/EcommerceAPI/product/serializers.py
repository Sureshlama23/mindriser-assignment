from rest_framework import serializers
from product.models import Category,Brand,Product,Cart,Orders

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['uid','brand_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderedPlacedSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Orders
        fields = ['uid','seller','buyer','product','quantity','shipping_fee','subtotal','ordered_date','updated_at','status','payment_status']
