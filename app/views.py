from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post



def post_list(request):
    instance = Post.objects.all()
    context ={
    "instance":instance
    }
    return render(request, "post_list.html", context)

def post_create(request):

    return HttpResponse("<h1>post_create</h1>")

def post_update(request, pk):
    return HttpResponse("<h1>post_update</h1>"+f"Update : {pk}")

def post_detail(request, pk):
    x = get_object_or_404(Post, id=pk)
    context={
    "object":x
    }
    return render(request, "post_detail.html", context)

def post_delete(request, pk):
    return HttpResponse("<h1>post_delete</h1>"+f"delete : {pk}")


