from django.shortcuts import render, redirect, get_object_or_404
from django.urls import include
from .models import Post
from .forms import PostForm


# Create your views here.


def base(request):
    all_write = Post.objects.all()
    return render(request, "writes/base.html", {'all_write': all_write})


def write(request):
    if request.method == "POST":
        write_form = PostForm(request.POST)
        if write_form.is_valid():
            write_form.save()
            return redirect("base/")
    else:
        write_form = PostForm()
    return render(request, "writes/write.html", {"write_form": write_form})
