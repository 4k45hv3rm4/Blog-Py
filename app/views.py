from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def post_list(request):
    instance = Post.objects.all()
    context ={
    "instance":instance
    }
    return render(request, "post_list.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
    "form":form
    }
    return render(request,"post_form.html", context)

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


