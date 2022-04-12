from multiprocessing import context
from shelve import Shelf
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookCreate

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    context = {"shelf": shelf}
    return render(request,'books/library.html',context)

def upload(request):
    upload = BookCreate()
    if request.method == "POST":
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid:
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" SOmething went wrong. Please reload 
            the webpage by clicking <a href="{{url:'index'}}">
            Reload </a> """)
    else:
        context_1 = {"upload_form":upload}
        return render (request,'books/upload_form.html',context_1)

def update_book(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None,instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request,'books/upload_form.html', {'upload_form':book_form})

def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')