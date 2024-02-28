from django.shortcuts import render
from product.models import Orders
from product.serializers import OrderedPlacedSerializer
from .models import Customer,User
from .serializers import CustomerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
# Create your views here.


class CustomerAddress(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self,request):
        email = self.request.user.email
        user = User.objects.get(email=email)
        add = self.get_queryset().filter(user=user.uid)
        serializer = self.serializer_class(add,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        email = self.request.user.email
        user = User.objects.get(email=email)
        customer_name = request.data.get('customer_name')
        locality = request.data.get('locality')
        city = request.data.get('city')
        zipcode = request.data.get('zipcode')
        zone = request.data.get('zone')
        number = request.data.get('number')
        data = {"user":user.uid,"customer_name":customer_name,"locality":locality,
                "city":city,"zipcode":zipcode,"zone":zone,"number":number}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
             serializer.save()
             return Response({"message": "Address added successfully"},status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors)
        
    def retrieve(self, request,uid):
         add = Customer.objects.get(uid=uid)
         serializer = self.serializer_class(add)
         return Response(serializer.data)
        
    def update(self,request,uid):
        try:
            add_update = Customer.objects.get(uid=uid)
            serializer = self.serializer_class(add_update,data=request.data,partial=True)
            if serializer.is_valid():
                 serializer.save()
                 return Response({"message": "Address update successfully"},status=status.HTTP_200_OK)
            else:
                 return Response(serializer.errors)    
        except:
             return Response({"error": "Data not found"},status=status.HTTP_204_NO_CONTENT)
            
    def destroy(self,request,uid):
          try:
               add = Customer.objects.get(uid=uid)
               add.delete()
               return Response({"message": "Address delete successfull"},status=status.HTTP_200_OK)
          except:
             return Response({"error": "Data not found"},status=status.HTTP_204_NO_CONTENT)
               
     

class customerOrderView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderedPlacedSerializer

    def list(self, request):
        user = User.objects.get(email=request.user.email)
        query = Q(Q(buyer__user=user.uid) & Q(payment_status='Not Done'))
        orders = Orders.objects.filter(query)
        amount = sum(order.subtotal for order in orders)
        data = {
            "items": OrderedPlacedSerializer(orders, many=True).data,
            "bill_to_pay": amount
        }
        return Response(data)


    
class PaymentOrderview(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderedPlacedSerializer

    def create(self, request):
        payment_amount = request.data.get('payment')
        user = User.objects.get(email=request.user.email)
        query = Q(Q(buyer__user=user.uid) & Q(payment_status='Not Done'))
        orders = Orders.objects.filter(query)
        print(orders)
        amount = sum(order.subtotal for order in orders)
        print(amount)
        if payment_amount == amount:
            for order in orders:
                order.payment_status= 'Done'
                order.save()
        
            return Response({"message": "Payment successfull"})
        else:
            return Response({"error": "Not enough balance"})