import re
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request,**kwargs):
    #posts = post.objects.all()
    #posts = post.objects.filter(status=1)
    posts=post.objects.filter(published_date__lte=timezone.now())
    if kwargs.get('cat_name') !=None:
        posts=posts.filter(category__name=kwargs['cat_name'])

    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)


    
def blog_single(request,pid):
    posts=get_object_or_404(post,id=pid,status=1)
    posts.counted_view=posts.counted_view+1
    posts.save()
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)

def test(request):
    #posts = post.objects.get(id=pid)
    #posts=get_object_or_404(post,id=pid)
    #posts.counted_view=posts.counted_view+1
    #posts.save()
    #posts = post.objects.all()
    #posts = post.objects.filter(status=0)
    #context={'posts':posts}
    return render(request,'test.html')

def blog_category(request, cat_name):
    posts=post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts=post.objects.filter(published_date__lte=timezone.now())

    if request.method == 'GET':
        if request.GET.get('s'):
            posts=posts.filter(content__contains=request.GET.get('s'))

    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
