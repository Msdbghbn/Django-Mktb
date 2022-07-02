from django.contrib import admin

from blog.models import post

class postAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','counted_view','status','created_date','published_date')
    list_filter=('status',)
    ordering=['-created_date']
    search_fields=['title','content']
admin.site.register(post, postAdmin)
# Register your models here.
