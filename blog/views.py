from django.shortcuts import render, get_object_or_404
from blog.models import post


def blog_view(request):
    #posts = post.objects.all()
    posts = post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request,pid):
    #posts = post.objects.get(id=pid)
    posts=get_object_or_404(post,id=pid)
    #posts = post.objects.all()
    #posts = post.objects.filter(status=0)
    context={'post':posts}
    return render(request,'test.html',context)