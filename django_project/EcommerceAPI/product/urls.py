from django.urls import path
from .views import *

urlpatterns = [
    path('category-create/',CategoryCreate.as_view(),name='category'),
    path('category-list/',CategoryList.as_view(),name='category-list'),
    path('category-update/<slug>',CategoryRetriveUpdate.as_view({'get':'retrieve','delete':'destroy'}),name='category-update'),
    path('brand-create/',BrandCreate.as_view(),name='brand-create'),
    path('brand-list/',BrandList.as_view(),name='brand-list'),
    path('brand-update/<slug>',BrandRetriveUpdate.as_view({'get':'retrieve','delete':'destroy'}),name='brand-update'),
    path('product-create/',ProductCreate.as_view(),name='product-create'),
    path('product-list/',ProductList.as_view(),name='product-list'),
    path('product-update/<slug>',ProductRetriveUpdate.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='product-update'),
    path('cart-list/',CartView.as_view({'get':'list','post':'create'}),name='cart-list'),
    path('cart-update/<uid>',CartView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='cart-update'),
    path('orders/',OrderPlacedView.as_view({'get':'list','post':'create'}),name='orders'),
]
