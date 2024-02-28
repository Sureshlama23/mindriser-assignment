from django.db import models
from user.models import User
from autoslug import AutoSlugField
from base.models import BaseModel
from customer.models import Customer
from shop.models import shopDetail
# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_slug = AutoSlugField(populate_from='category_name',unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='Category_img')

    def __str__(self):
        return self.category_name

class Brand(BaseModel):
    brand_name = models.CharField(max_length=100)
    brand_slug = AutoSlugField(populate_from='brand_name',unique=True,null=True,blank=True)

    def __str__(self):
        return self.brand_name
    
class Product(BaseModel):
    seller = models.ForeignKey(shopDetail,on_delete=models.PROTECT,related_name='Product_seller')
    product_name = models.CharField(max_length=100)
    selling_price = models.PositiveIntegerField(default=1)
    discount_price = models.PositiveIntegerField(default=1)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_img')
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='product_category')
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='product_brand')
    product_slug = AutoSlugField(populate_from='product_name',unique=True,blank=True,null=True)
    
    def __str__(self):
        return self.product_name

class Cart(BaseModel):
    buyer = models.ForeignKey(User,on_delete=models.PROTECT,related_name='cart_user')
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name="carts_product")
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
    @property
    def seller(self):
        return self.product.seller
    
    def __str__(self):
        return f"{self.buyer.username,self.product.product_name,self.quantity}"
    


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel'),
)
PAYMENT_CHECK = (
    ("Not Done","Not Done"),
    ("Done","Done")
)
class Orders(BaseModel):
    cart = models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True)
    seller = models.ForeignKey(shopDetail,on_delete=models.PROTECT)
    buyer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='orders')
    quantity = models.PositiveIntegerField(default=0)
    shipping_fee = models.IntegerField(default=50)
    subtotal = models.PositiveIntegerField(default=0)
    ordered_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=20,default='Pending')
    payment_status = models.CharField(max_length=20,choices=PAYMENT_CHECK,null=True,default='Not Done')

    class Meta:
      ordering = ['-ordered_date']




    



    


