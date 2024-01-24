from django.shortcuts import render,redirect
from .models import Book

# Create your views here.


# This function will add new object and Show all objects
def addView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        ISBN = request.POST.get('ISBN')
        description = request.POST.get('description')
        file = request.POST.get('file')
        book_obj = Book.objects.create(title=title,author=author,published_date=published_date,ISBN=ISBN,description=description,file=file)
        book_obj.save()
        return redirect('addandshow')
    
    else:
        book_objs = Book.objects.all()
        content = {'books':book_objs}
        return render(request,'addandshow.html',context=content)
    
# This function will update object
def update(request,id):
    book_obj = Book.objects.get(id=id)
    mes = None
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        ISBN = request.POST.get('ISBN')
        description = request.POST.get('description')
        file = request.POST.get('file')
        book_obj.title = title
        book_obj.author = author
        book_obj.published_date = published_date
        book_obj.ISBN = ISBN
        book_obj.description = description
        book_obj.file = file
        book_obj.save()
        mes = 'Book info update success '
        return redirect('addandshow')
    data = {'book':book_obj,'message': mes}
    return render(request,'update.html',data)

# This function will delete object
def delete(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.delete()
    return redirect('addandshow')

    




    



    
