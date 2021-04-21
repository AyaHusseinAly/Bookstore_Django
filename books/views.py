from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book

def index(request):
    books= Book.objects.all()
    return render(request,"books/index.html",{
        "books":books
    })

def create(request):
    book= BookForm(request.POST or None)
    if book.is_valid():
        book.save()
        return redirect("index")
    return render(request,"books/create.html",{'form':book})    


def edit(request,id):
    bookData=Book.objects.get(pk=id)
    book= BookForm(request.POST or None, instance=bookData)
    if book.is_valid():
        book.save()
        return redirect("index")
    return render(request,"books/edit.html",{'form':book, "data":bookData})    

def delete(request,id):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect("index")

def view(request,id):
    book=Book.objects.get(pk=id)
    return render(request,"books/view.html",{
        "book":book
    })