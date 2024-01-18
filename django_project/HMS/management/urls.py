from django.urls import path
from management.views import EmployeeInfoView

urlpatterns = [
    path('employee-info/all/',EmployeeInfoView.as_view({'get':'list','post':'create'}),name='employee-info'),
]
