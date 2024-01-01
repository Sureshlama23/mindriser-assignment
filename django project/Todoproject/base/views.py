from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todoproject

# Create your views here.
def home(request):
    todos = Todoproject.objects.all()
    content = {'todos': todos}
    return render(request,'index.html',context=content)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todoproject.objects.create(name=name,description=description,status=status)
        return redirect('home')
    content = {'mode':'create'}
    return render(request,'create.html',context=content)
def edit(request,id):
    todo = Todoproject.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.name = name
        todo.description = description
        todo.status = status
        todo.save()
        return redirect('home')

    content = {'mode': 'edit','todo':todo}
    return render(request,'create.html',context=content)
def delete(request,id):
    todo = Todoproject.objects.get(id=id)
    todo.delete()
    return redirect('home')
def deleteAll(request):
    todo = Todoproject.objects.all()
    todo.delete()
    return redirect('home')