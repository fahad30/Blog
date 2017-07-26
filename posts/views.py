from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Done")
        return redirect("posts:list")
    context = {
        "form":form,
     }
    return render(request, 'post_create.html', context)


def post_detail(request, post_id):
    object_list = Post.objects.all()#.order_by("-timestamp", "-updated")
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Detail",
    "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()
    context = {
    "title": "List",
    "object_list": object_list
    }
    return render(request, 'post_list.html', context)

def post_update(request, post_id):
    post_object = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Cool")
        return redirect("posts:list")
    context = {
        "form":form,
        "post_object":post_object,
     }
    return render(request, 'post_update.html', context)

def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    messages.warning(request, "really")
    return redirect("posts:list")
































    