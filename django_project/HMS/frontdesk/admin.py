from django.contrib import admin
from .models import GuestInfo,GuestRoom

# Register your models here.
class GuestInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','Phone_no', 'address','email']

admin.site.register(GuestInfo,GuestInfoAdmin)
admin.site.register(GuestRoom)
