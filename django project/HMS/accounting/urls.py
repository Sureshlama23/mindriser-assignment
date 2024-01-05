from django.urls import path
from .views import bill_view

urlpatterns = [
    path('bill/all/',bill_view,name='bill-list')
]
 