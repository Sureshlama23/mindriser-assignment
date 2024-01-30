from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


STATE_CHOICES = (('Bagmati','Bagmati'),
('Koshi','Koshi'),
('Madhesh','Madhesh'),
('Gandaki','Gandaki'),
('Lumbini','Lumbini'),
('Karnali','Karnali'),
('Sudurpashchim','Sudurpashchim'))



# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    locality = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=60)



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = AutoSlugField(populate_from='category_name',unique=True,null=True,default=None)
    image = models.ImageField(upload_to='Category_imgs',null=True)


    def __str__(self):
        return self.category_name

class Brand(models.Model):
    category_type = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="brand_category")
    brand_name = models.CharField(max_length=100)
    brand_slug = AutoSlugField(populate_from='brand_name',unique=True,null=True,default=None)

    def __str__(self):
        return f"{self.brand_name} {self.category_type.category_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    selling_price = models.PositiveIntegerField(default=1)
    discount_price = models.PositiveIntegerField(default=1)
    Product_description = models.TextField()
    product_image = models.ImageField(upload_to='products_imgs')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='productBrand_Category')
    product_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cart')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.PositiveIntegerField(default=1)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_user')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order_customer')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_product')
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)