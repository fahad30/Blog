from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_create(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "Create",
    "user": request.user
    }
    return render(request, 'post_create.html', context)

from django.shortcuts import get_object_or_404

def post_detail(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Detail",
    "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "List",
    "user": request.user
    }
    return render(request, 'post_list.html', context)

def post_update(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "Update",
    "user": request.user
    }
    return render(request, 'post_update.html', context)

def post_delete(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "delete",
    "user": request.user
    }
    return render(request, 'post_delete.html', context)


















