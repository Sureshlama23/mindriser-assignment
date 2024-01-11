from .views import login,create_owner
from django.urls import path

urlpatterns = [
    path('login/',login,name='login'),
    path('create-owner/',create_owner,name='create-owner'),
]