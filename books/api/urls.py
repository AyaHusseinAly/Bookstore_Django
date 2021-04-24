from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index),
    path("create", views.create),
    path("view/<int:id>", views.view),
    path("edit/<int:id>", views.edit),
    path("delete/<int:id>", views.delete),

    path("login", obtain_auth_token),
    path("signup", views.signup),
    



]