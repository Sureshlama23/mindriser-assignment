from .views import login,create_owner,group_list
from django.urls import path

urlpatterns = [
    path('login/',login,name='login'),
    path('create-owner/',create_owner,name='create-owner'),
    path('group/all/',group_list,name='group'),
]