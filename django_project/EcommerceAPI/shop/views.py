from django.shortcuts import render
from rest_framework import status
from user.models import User
from rest_framework.response import Response
from product.serializers import OrderedPlacedSerializer
from product.models import Orders
from .models import shopDetail
from .serializers import shopDetailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from django.db.models import Q
# Create your views here.

class ShopDetailView(ModelViewSet):
    queryset = shopDetail.objects.all()
    serializer_class = shopDetailSerializer

    def list(self,request):
        if self.request.user.groups.filter(name="Owner").exists():
            shop_detail = self.get_queryset()
            serializer = self.serializer_class(shop_detail,many=True)
            return Response(serializer.data)
        else:
            email = self.request.user.email
            user = User.objects.get(email=email)
            shop_detail = self.get_queryset().filter(user=request.user.uid)
            serializer = self.serializer_class(shop_detail,many=True)
            return Response(serializer.data)
    
    def create(self,request):
        email = self.request.user.email
        user = User.objects.get(email=email)
        name = request.data.get('name')
        number = request.data.get('number')
        address = request.data.get('address')
        number = request.data.get('number')
        data = {"user":user.uid,"name":name,"number":number,"address":address}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New Shop detail added successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def retrieve(self, request,uid):
        try:
            shop_detail = shopDetail.objects.get(uid=uid)
            serializer = self.serializer_class(shop_detail)
            return Response(serializer.data)   
        except:
            return Response({"error": "No data found"},status=status.HTTP_204_NO_CONTENT)
          
    def update(self, request,uid):
        try:
            shop_detail = shopDetail.objects.get(uid=uid)
            serializer = self.serializer_class(shop_detail,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Shop detail update successfull"},status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors)
        
        except:
            return Response({"error": "No data found"},status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request,uid):
        try:
            shop_detail = shopDetail.objects.get(uid=uid)
            shop_detail.delete()
            return Response({"message": "Shop detail delete successfull"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"error": "No data found"},status=status.HTTP_204_NO_CONTENT)
        
class shopOrderView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderedPlacedSerializer

    def list(self, request):
        user = User.objects.get(email=request.user.email)
        query = Q(Q(seller__user=user.uid) & Q(payment_status='Not Done'))
        orders = Orders.objects.filter(query)
        amount = sum(order.subtotal for order in orders)
        data = {
            "items": OrderedPlacedSerializer(orders, many=True).data,
            "bill_to_pay": amount
        }
        return Response(data)
    
    def retrieve(self, request,uid):
        order = Orders.objects.get(uid=uid)
        serializer = OrderedPlacedSerializer(order)
        return Response(serializer.data)
    
    def update(self, request,uid):
        order = Orders.objects.get(uid=uid)
        serializer = self.serializer_class(order,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product status update successfull"},status=status.HTTP_200_OK)
        else:
           return Response(serializer.errors)