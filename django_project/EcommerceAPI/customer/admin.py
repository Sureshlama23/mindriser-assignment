from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmint(admin.ModelAdmin):
    list_display = ['uid','user','customer_name','city','zipcode','zone','number','customer_slug']