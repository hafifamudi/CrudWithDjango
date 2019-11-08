from django.shortcuts import render
from django.shortcuts import redirect

from .models import BookList
# Create your views here

def index(request):
    books = BookList.objects.all()
    return render(request,'index.html',{'books':books})

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author= request.GET['author']
    book_details = BookList(title=title,price=price,author=author)
    book_details.save()
    return redirect('/')

def add_book(request):
    return render(request, 'add_book.html')

def edit(request, id):
    books = BookList.objects.get(pk=id)
    context = {
        'books' : books
    }
    return render(request,'edit.html',context)

def delete(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def update(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')