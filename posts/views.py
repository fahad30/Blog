from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.http import Http404
def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Done")
        return redirect("posts:list")
    context = {
        "form":form,
     }
    return render(request, 'post_create.html', context)

def post_detail(request, slug):
    object_list = Post.objects.all()
    instance = get_object_or_404(Post, slug=slug)
    context = {
    "title": "Detail",
    "instance": instance,
     "share_string": quote(instance.content)
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()#.order_by("-timestamp", "-updated")

    paginator = Paginator(object_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    context = {
    "title": "List",
    "object_list": objects
    }
    return render(request, 'post_list.html', context)

def post_update(request, slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404

    post_object = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_object)
    if form.is_valid():
        form.save()
        messages.success(request, "Cool")
        return redirect("posts:list")
    context = {
        "form":form,
        "post_object":post_object,
     }
    return render(request, 'post_update.html', context)

def post_delete(request, slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404

    Post.objects.get(slug=slug).delete()
    messages.warning(request, "really")
    return redirect("posts:list")

















    