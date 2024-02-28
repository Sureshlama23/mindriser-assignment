from django.contrib import admin
from .models import shopDetail

# Register your models here.
@admin.register(shopDetail)
class shopDetailAdmin(admin.ModelAdmin):
    list_display = ['uid','user','name','address','number']