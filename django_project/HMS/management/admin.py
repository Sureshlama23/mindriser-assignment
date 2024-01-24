from django.contrib import admin
from .models import EmployeeInfo,Room,RoomType
from user.models import User
from django.contrib import admin

# Register your models here.
class EmployeeInfoAdmin(admin.ModelAdmin):
    email = User()
    list_display = ['id','name','number','photo','email']

admin.site.register(EmployeeInfo,EmployeeInfoAdmin)

class RoomAdmin(admin.ModelAdmin):
    type = RoomType()
    list_display = ['id','room_no','floor','description','type']

admin.site.register(Room,RoomAdmin)
class RoomTypeAdmin(admin.ModelAdmin):
    type = RoomType()
    list_display = ['id','name']

admin.site.register(RoomType,RoomTypeAdmin)