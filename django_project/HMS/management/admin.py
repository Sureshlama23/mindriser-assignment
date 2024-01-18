from django.contrib import admin
from .models import EmployeeInfo

# Register your models here.
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','number','photo']

admin.site.register(EmployeeInfo,EmployeeInfoAdmin)