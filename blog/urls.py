
from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed
app_name = 'blog'
urlpatterns = [ path('',blog_view,name='blog_index'),
                path('<int:pid>',blog_single,name='single'),
                path('test',test,name='test'),
                path('category/<str:cat_name>',blog_view,name='category'),
                path('author/<str:aut_username>',blog_view,name='author'),
                path('search/',blog_search,name='search'),
                path('tag/<str:tag_name>',blog_view,name='tag'),
                path('rss/feed/',LatestEntriesFeed())
                #path('<str:name>',test,name='test')


]  




