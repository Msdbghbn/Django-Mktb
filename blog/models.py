from django.db import models
from traitlets import default
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class post(models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=250) 
    content=models.TextField()
    counted_view = models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)
    category=models.ManyToManyField(Category)

    tags=TaggableManager()

    def __str__(self):
        return "{} , {}".format(self.title, self.id)
    
    #def snippets(self):
     #   return self.content[:100] + '...'
