from .views import login
from django.urls import path

urlpatterns = [
    path('login/',login,name='login'),
]