from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
def post_create(request, post_id):
    object_list = Post.objects.all()
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Create",
    "instance": instance
    }
    return render(request, 'post_create.html', context)


def post_detail(request, post_id):
    object_list = Post.objects.all()
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Detail",
    "instance": instance
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()
    # instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "List",
    "object_list": object_list
    }
    return render(request, 'post_list.html', context)

def post_update(request, post_id):
    object_list = Post.objects.all()
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Update",
    "instance": instance
    }
    return render(request, 'post_update.html', context)

def post_delete(request, post_id):
    object_list = Post.objects.all()
    instance = get_object_or_404(Post, id=post_id)
    context = {
    "title": "Delete",
    "instance": instance
    }
    return render(request, 'post_delete.html', context)

















