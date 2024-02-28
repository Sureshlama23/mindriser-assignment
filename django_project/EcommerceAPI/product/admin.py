from django.contrib import admin
from .models import Category,Brand,Product,Cart,Orders

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['uid','category_name','category_slug','image']
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['uid','brand_name','brand_slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['uid','seller','product_name','selling_price','discount_price',
                    'description','product_image','category','brand','product_slug']
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['uid','buyer','seller','product','quantity','total_cost']

@admin.register(Orders)
class OrderedPlacedAdmin(admin.ModelAdmin):
    list_display = ['uid','seller','buyer','product','quantity','shipping_fee','subtotal','ordered_date','updated_at','status','payment_status']
