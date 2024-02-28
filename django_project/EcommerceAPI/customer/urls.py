from django.urls import path
from .views import CustomerAddress,customerOrderView,PaymentOrderview

urlpatterns = [
    path('buyer-orders/',customerOrderView.as_view({'get':'list'}),name='buyer-orders'),
    path('payment/',PaymentOrderview.as_view({'post':'create'}),name='payment'),
    path('profile/',CustomerAddress.as_view({'get':'list','post':'create'}),name='profile'),
    path('profile-update/<uid>',CustomerAddress.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='profile-update'),
]
