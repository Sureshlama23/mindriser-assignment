from django.shortcuts import render,redirect
from .models import Category,Product,Customer,Cart
from django.views import View
from .forms import CustomerRegistrationForm,CustomerForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout



categories = Category.objects.all

# Create your views here.
def home(request,slug=None):
    products = Product.objects.all()
    mode = None
    cart_objs_num = None
    if request.user.is_authenticated:
        user = request.user
        cart_objs_num = Cart.objects.filter(user=user).order_by('id')
    if slug != None:
        products = Product.objects.filter(category__category_name__icontains=slug)
        mode='categoryproduct'
    if request.method == 'GET':
        query = request.GET.get('product_name')
        if query is not None:
            multiple_query = Q(Q(product_name__icontains=query) | Q(brand__brand_name__icontains=query) | Q(category__category_name__icontains=query))
            products = Product.objects.filter(multiple_query)
            mode='productsonly'
    data = {'categories': categories,'products':products,'mode':mode,'cart_objs_num':cart_objs_num}
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

class ShoppingCartView(View):
    subtotal = 0.00
    shipping_amount = 50
    Total_amount = 0.00
    coupon = "10%-off"
    products = Product.objects.all()
    def get(self,request,slug=None):
        user = request.user
        # add to cart
        if slug is not None:
            product_add_to_cart = Product.objects.get(product_slug=slug)
            try:
                cart = Cart.objects.get(Q(product=product_add_to_cart) & Q(user=user))
                cart.quantity +=1
                cart.save()
            except:
                cart_product_obj = Cart.objects.create(user=user,product=product_add_to_cart)
                cart_product_obj.save()
        # add to cart end
        
        cart_products = [ p for p in Cart.objects.all() if request.user == user]
        if cart_products: 
            for p in cart_products:
                temp_amount = (p.product.discount_price * p.quantity)
                self.subtotal += temp_amount 
                Total_amount = self.subtotal + self.shipping_amount
        cart_product = Cart.objects.filter(user=user)
        data = {'categories': categories,'products':self.products,'cart_products':cart_product,
                    'subtotal':self.subtotal,'total_amount':Total_amount,'shipping_amount':self.shipping_amount}
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
    
class ProfileView(View):
    def get(self,request):
        products = Product.objects.all()
        form =CustomerForm()
        data = {'categories': categories,'products':products,'form':form}
        return render(request,'profile.html',data)
    def post(self,request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            number = form.cleaned_data['number']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode,number=number)
            reg.save()
            messages.success(request,'Profile Update Successfully')
        else:
            messages.error(request,'Profile Update remain same')
        return render(request,'profile.html')

class AddressView(View):
    def get(self,request):
        address = Customer.objects.filter(user=request.user)
        products = Product.objects.all()
        data = {'categories': categories,'products':products,'addresses':address}
        return render(request,'address.html',data)
    
def logout_user(request):
    logout(request)
    messages.success(request,"You are logout")
    return redirect('home')
