from logging import root
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404, HttpResponseRedirect
from django.http import Http404, HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.db.models import Q
import os

def like_view(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post:detail', args=[str(post.slug)]))

def liked_view(request):
    post = Post.objects.all() 
    posts = []
    for i in post:
        for a in i.likes.all():
            if str(a) == str(request.user.username):
                posts.append(i)
    return render(request,'post/liked.html',{'posts': posts})

def post_index(request):
    posts = Post.objects.all() 
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
                            Q(title__icontains=query) | 
                            Q(content__icontains=query)|
                            Q(user__first_name__icontains=query)|
                            Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(posts, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'post/index.html',{'posts':page_obj})

def category_view(request, cats):
    posts = Post.objects.all() 
    context = {
        'cats': cats,
        'posts' : posts,
    }
    return render(request, 'categories/categories.html',context)

def post_home(request):
    posts = Post.objects.all() 
    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query) | 
                            Q(content__icontains=query)|
                            Q(user__first_name__icontains=query)|
                            Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(posts, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'posts':page_obj})


def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)#içerik varsa verileri dönder(post için), yoksa boş dönder(get için).
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()        
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post':post,
        'form':form,
        'count_like': post.number_of_likes
    }
    
    return render(request,'post/detail.html',context)

def post_create(request):
    if not request.user.is_authenticated:
        return Http404()
    form = PostForm(request.POST or None, request.FILES or None)#içerik varsa verileri dönder(post için), yoksa boş dönder(get için).
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request,'başarılı bir şekilde oluşturuldu',extra_tags='mesaj-basarılı')
        
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)

def post_update(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.FILES:
        os.remove(post.image.path)
    if form.is_valid() and request.user.username == post.user.username:
        post = form.save()
        messages.success(request,'başarılı bir şekilde güncellendi')
        
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }   
    return render(request, 'post/form.html', context)

def post_delete(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    if request.user.username == post.user.username:
        post.delete()
        messages.success(request,'başarılı bir şekilde silindi')
    
    return redirect('post:index')