from django.shortcuts import render
from django.http import HttpResponse
from .models import Todoproject

# Create your views here.
def home(request):
    todos = Todoproject.objects.all()
    print(todos)
    return render(request,'index.html')