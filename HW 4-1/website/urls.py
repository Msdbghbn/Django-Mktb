from django.contrib import admin
from django.urls import path, include
from website.views import *


from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [path('',index_view,name='index'),path('home',index_view,name='index') ,path('about',about_view,name='about'), path('contact',contact_view,name='contact'),
            path('portfolio',portfolio_view,name='portfolio'),path('testmonial',testmonial_view,name='testmonial'), path('blog',blog_view,name='blog') ]  



