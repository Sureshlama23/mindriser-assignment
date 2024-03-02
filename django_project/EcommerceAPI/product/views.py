from django.shortcuts import render
from .models import Category,Brand,Product,Cart,Orders,User
from .serializers import CategorySerializer,BrandSerialzier,ProductSerializer,CartSerializer,OrderedPlacedSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import AllowAny
from core.custompermission import CustomPermissions
from rest_framework import status
from django.db.models import Q
from shop.models import shopDetail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .paginations import ListPagination


# Create your views here.
class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class CategoryRetriveUpdate(ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = [CustomPermissions]


        def retrieve(self,request,slug):
            try:
                cat_obj = Category.objects.get(category_slug=slug)
                serializer = self.serializer_class(cat_obj)
                return Response(serializer.data)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)
        
        def destroy(self, request,slug):
            try:
                cat_obj = Category.objects.get(category_slug=slug)
                cat_obj.delete()
                return Response({"message":"Category delete successfull"},status=status.HTTP_202_ACCEPTED)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)

class BrandCreate(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerialzier
    permission_classes = [CustomPermissions]


class BrandList(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerialzier
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand']

class BrandRetriveUpdate(ModelViewSet):
        queryset = Brand.objects.all()
        serializer_class = BrandSerialzier
        permission_classes = [CustomPermissions]

        def retrieve(self,request,slug):
            try:
                cat_obj = Brand.objects.get(brand_slug=slug)
                serializer = self.serializer_class(cat_obj)
                return Response(serializer.data)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)
        
        def destroy(self, request,slug):
            try:
                cat_obj = Brand.objects.get(brand_slug=slug)
                cat_obj.delete()
                return Response({"message":"Brand delete successfull"},status=status.HTTP_202_ACCEPTED)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)
     
            

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['^product_name','^description']
    pagination_class = ListPagination

class ProductRetriveUpdate(ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = [CustomPermissions]


        def retrieve(self,request,slug):
            try:
                pro_obj = Product.objects.get(product_slug=slug)
                serializer = self.serializer_class(pro_obj)
                return Response(serializer.data)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)
            
        def update(self,request,slug):
             email = self.request.user.email
             user = User.objects.get(email=email)
             shop_uid = shopDetail.objects.get(user_email=email)
             pro = Product.objects.get(Q(seller=shop_uid) & Q(product_slug=slug))
             print(pro)
             pro_obj = Product.objects.get(product_slug=slug)
             serializer = self.serializer_class(pro_obj,data=request.data,partial=True)
             if serializer.is_valid():
                  serializer.save()
                  return Response({"message": "Product details update successfull"},status=status.HTTP_200_OK)
             else:
                  return Response(serializer.errors)
             
        
        def destroy(self, request,slug):
            try:
                pro_obj = Product.objects.get(product_slug=slug)
                pro_obj.delete()
                return Response({"message":"Product delete successfull"},status=status.HTTP_202_ACCEPTED)
            except:
                 return Response({"error":"Data not found"},status=status.HTTP_204_NO_CONTENT)
            
            
class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = ListPagination

    def list(self,request):
        query = Q(Q(product__seller__user=self.request.user) | Q(buyer=self.request.user))
        cart_objs = Cart.objects.filter(query)
        serializer = self.serializer_class(cart_objs,many=True)
        return Response(serializer.data) 
    
    def create(self,request):
        email = self.request.user.email
        user = User.objects.get(email=email)
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        data = {"buyer":user.uid,"product":product,"quantity":quantity}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
             serializer.save()
             return Response({"message": "Product add to cart successfully"},status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors)
        
    def retrieve(self,request,uid):
         try:
            cart_obj = Cart.objects.get(uid=uid)
            serializer = self.serializer_class(cart_obj)
            return Response(serializer.data)
         except:
            return Response({"error": "No data found!"})
         
    def update(self,request,uid):
        cart_obj = Cart.objects.get(uid=uid)
        serializer = self.serializer_class(cart_obj,data=request.data,partial=True)
        if serializer.is_valid():
             serializer.save()
             return Response({"message": "Cart update successfully"},status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors)
        
    def destroy(self, request,uid):
         try:
            del_cart_obj = Cart.objects.get(uid=uid)
            del_cart_obj.delete()
            return Response({"message": "Cart object delete successfull"},status=status.HTTP_200_OK)
         except:
              return Response({"error": "Data not found!"},status=status.HTTP_204_NO_CONTENT)
    
class OrderPlacedView(ModelViewSet):
     queryset = Orders.objects.all()
     serializer_class = OrderedPlacedSerializer
     pagination_class = ListPagination


     def list(self,request):
        user = User.objects.get(email=self.request.user.email)
        query = Q(Q(seller__user=user.uid) | Q(buyer__user=user.uid))
        order_obj = self.get_queryset().filter(query)
        serializer = self.serializer_class(order_obj,many=True)
        return Response(serializer.data)          
     
     def create(self,request):
        email = self.request.user.email
        address_uid = request.data.get('address')
        buyer = User.objects.get(email=email)
        cart = Cart.objects.filter(buyer=buyer)
        shipping_fee = 50
        if cart.exists():
             for c in cart:
                subtotal = (c.product.discount_price * c.quantity)
                data = {'cart':c.uid,'seller':c.product.seller.uid,'buyer':address_uid,'product':c.product.uid,'quantity':c.quantity,'subtotal':shipping_fee + subtotal}
                serializer = OrderedPlacedSerializer(data=data)
                if serializer.is_valid():
                     serializer.save()
                else:
                     return Response(serializer.errors)
             cart.delete()
             return Response({"message": "Your order accepted"},status=status.HTTP_202_ACCEPTED)  
        else:
             return Response({"message": "Your cart is empty"},status=status.HTTP_204_NO_CONTENT)


        
