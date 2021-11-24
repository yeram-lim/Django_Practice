from django.contrib import admin
from django.urls import path
from . import views

app_name = 'writes'
urlpatterns = [
    path("", views.base, name="base"),
    path("/", views.write, name="write"),
    path("/base/", views.base, name="base2"),
]
