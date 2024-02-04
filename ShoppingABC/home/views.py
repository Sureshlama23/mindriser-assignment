from django.shortcuts import render,redirect
from .models import Category,Brand,Product
from django.views import View
from .forms import CustomerRegistrationForm,LoginForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout


categories = Category.objects.all

# Create your views here.
def home(request,slug=None):
    products = Product.objects.all()
    mode = None
    if slug != None:
        products = Product.objects.filter(category__category_name__icontains=slug)
        mode='productsonly'
    if request.method == 'GET':
        query = request.GET.get('product_name')
        if query is not None:
            multiple_query = Q(Q(product_name__icontains=query) | Q(brand__brand_name__icontains=query) | Q(category__category_name__icontains=query))
            products = Product.objects.filter(multiple_query)
            mode='productsonly'
    data = {'categories': categories,'products':products,'mode':mode}
    return render(request,'index.html',data)
class shopView(View):
    def get(self,request):
        products = Product.objects.all()
        if request.method == 'GET':
            query = request.GET.get('product_name')
            if query is not None:
                multiple_query = Q(Q(product_name__icontains=query) | Q(brand__brand_name__icontains=query) | Q(category__category_name__icontains=query))
                products = Product.objects.filter(multiple_query)
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
class CustomerRegistrationView(View):
    def get(self,request):
        products = Product.objects.all()
        form = CustomerRegistrationForm()
        data = {'categories': categories,'products':products,'form':form}
        return render(request,'register.html',data)
    
    def post(self,request):
        products = Product.objects.all()
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'New Registration Successfull!')
            form.save()
        data = {'categories': categories,'products':products,'form':form}
        return render(request,'register.html',data)

def profileView(request):
    products = Product.objects.all()
    data = {'categories': categories,'products':products} 
    return render(request,'profile.html')

    
def logout_user(request):
    logout(request)
    messages.success(request,"You are logout")
    return redirect('home')
