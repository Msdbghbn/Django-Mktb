from tabnanny import verbose
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post,Category

class postAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','author','counted_view','status','created_date','published_date')
    list_filter=('status','author')
    ordering=['-created_date']
    search_fields=['title','content']
    summernote_fields = ('content',)

class Meta:
    ordering = ['created_date']
    #verbose_name='پست'   
    #verbose_name_plural='پست ها'

admin.site.register(post, postAdmin)
admin.site.register(Category)
# Register your models here.
