from django.shortcuts import render
from django.http import HttpResponse
from .models import Todoproject

# Create your views here.
def home(request):
    todos = Todoproject.objects.all()
    content = {'todos': todos}
    return render(request,'index.html',context=content)

def create(request):
    return render(request,'create.html')