from django.shortcuts import render
from .models import Category,Brand,Product
from django.views import View

categories = Category.objects.all

# Create your views here.
class homeView(View):
    def get(self,request):
        products = Product.objects.all()
        mode = None
        if request.method == 'GET':
            query_by_name = request.GET.get('product_name')
            if query_by_name is not None:
                products = Product.objects.filter(product_name__icontains=query_by_name)
                mode='productsonly'
        data = {'categories': categories,'products':products,'mode':mode}
        return render(request,'index.html',data)
class shopView(View):
    def get(self,request):
        products = Product.objects.all()
        if request.method == 'GET':
            query = request.GET.get('product_name')
            lowest_price = request.GET.get('low_price')
            if query is not None:
                products = Product.objects.filter(product_name__icontains=query)
            elif lowest_price is not None:
                products = Product.objects.all().order_by('-discount_price')
        data = {'categories': categories,'products':products}
        return render(request,'shop.html',data)

class productDetailView(View):
    def get(self,request,slug):
        product = None
        if slug is not None:
            product = Product.objects.get(product_slug=slug)
            mode = 'single_detail'
        data = {
            'categories': categories,'product':product}
        return render(request,'detail.html',data)

def shoppingCart(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products}
    return render(request,'cart.html',data)

def checkout(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products}
    return render(request,'checkout.html',data)

def contact(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products}
    return render(request,'contact.html',data)
def register(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products}
    return render(request,'register.html',data)
def login(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products}
    return render(request,'profile.html',data)
