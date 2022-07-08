from django import template
from blog.models import post
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

