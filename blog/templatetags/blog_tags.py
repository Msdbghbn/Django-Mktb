from unicodedata import category
from django import template
from blog.models import post
from blog.models import Category
from blog.models import Comments
register = template.Library()

@register.simple_tag(name='tp')
def function():
    posts_num=post.objects.filter(status=1).count()
    return posts_num

@register.simple_tag(name='posts')
def function():
    posts=post.objects.filter(status=1)
    return posts
@register.filter
def snippet(value,arg=15):
    return value[:arg]+'...'

@register.inclusion_tag('blog/blog-popularposts.html')
def popularposts(arg=3):
    posts = post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-num-postcategories.html')
def numpostcats():
    posts = post.objects.filter(status=1)
    cats=Category.objects.all()
    cat_post={}
    for name in cats:
        cat_post[name]=posts.filter(category=name).count()
    return {'categories':cat_post}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comments.objects.filter(post=pid,approved=True).count()
    

