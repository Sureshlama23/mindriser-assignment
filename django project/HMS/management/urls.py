from django.urls import path
from user.views import employeeInfoView

urlpatterns = [
    path('employee-user/',employeeInfoView,name='employee-user')
]
