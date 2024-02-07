from django.contrib import admin
from home.models import Customer,Category,Brand,Product,Cart,OrderPlaced

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','name','locality','city','zipcode','state','number']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name','category_slug','image']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','brand_name','brand_slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','selling_price','discount_price','product_description','product_image','brand','category']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderedPlacedAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date']

