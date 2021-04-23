from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import ContentType, Permission
from django.contrib.auth.models import User
from books.models import Book


def signup(request):
    
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user=authenticate(username=username, password=password)
        if user:
            contentType = ContentType.objects.get_for_model(Book)
            perms = Permission.objects.filter(content_type=contentType)
            u=User.objects.last()
            for perm in perms:
                u.user_permissions.add(perm)
            login(request,user)
            return redirect("index")
    return render(request,"registration/signup.html",{'form':form})