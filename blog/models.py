from statistics import mode
from django.db import models
from traitlets import default
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    category = models.ManyToManyField(Category)

    tags = TaggableManager()

    def __str__(self):
        return "{} , {}".format(self.title, self.id)

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})

    # def snippets(self):
     #   return self.content[:100] + '...'
class Comment(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    approved=models.BooleanField(default=False)

    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return self.name