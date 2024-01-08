from sys import path_hooks
from zipfile import Path
from django.urls import path
from .views import BillView

urlpatterns = [
    # path('bill/all/',bill_view,name='bill-list')
    path('bill/all/',BillView.as_view({'get':'list','post':'create'}),name='bill-list'),
    path('bill/<int:pk>',BillView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='bill-details'),
]
 