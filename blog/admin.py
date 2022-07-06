from tabnanny import verbose
from django.contrib import admin

from blog.models import post

class postAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','author','counted_view','status','created_date','published_date')
    list_filter=('status','author')
    ordering=['-created_date']
    search_fields=['title','content']

class Meta:
    ordering = ['created_date']
    #verbose_name='پست'   
    #verbose_name_plural='پست ها'
admin.site.register(post, postAdmin)
# Register your models here.
