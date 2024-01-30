from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class BookView(APIView):
    def get(self,request,pk=None,format=None):
        try:
            id =pk
            if id is not None:
                book_obj = Book.objects.get(id=id)
                serializer =BookSerializer(book_obj)
                return Response(serializer.data)

            book_objs = Book.objects.all()
            serializer = BookSerializer(book_objs,many=True)
            return Response(serializer.data)
        except:
            return Response({'message':'No data found'},status=status.HTTP_204_NO_CONTENT)
    
    def post(self,request,format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'New book added'},status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors)
        
    def put(self,request,pk,format=None):
        id = pk
        book_obj = Book.objects.get(id=id)
        serializer = BookSerializer(book_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        id = pk
        book_obj = Book.objects.get(id=id)
        serializer = BookSerializer(book_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        id = pk
        try:
            book_obj = Book.objects.get(id=id)
            book_obj.delete()
            return Response({'message': 'Data deleted'})        
        except:
            return Response({'message': 'No data found'},status=status.HTTP_400_BAD_REQUEST)
        
def home(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj,many=True)
    return render(request,serializer.data,'index.html')
