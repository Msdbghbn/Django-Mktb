from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone

def blog_view(request):
    #posts = post.objects.all()
    #posts = post.objects.filter(status=1)
    posts=post.objects.filter(published_date__lte=timezone.now())
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=get_object_or_404(post,id=pid,status=1)
    posts.counted_view=posts.counted_view+1
    posts.save()
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    #posts = post.objects.get(id=pid)
    posts=get_object_or_404(post,id=pid)
    posts.counted_view=posts.counted_view+1
    posts.save()
    #posts = post.objects.all()
    #posts = post.objects.filter(status=0)
    context={'posts':posts}
    return render(request,'test.html',context)

