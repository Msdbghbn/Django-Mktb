from django.db import models
from traitlets import default

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=250) 
    content=models.TextField()
    counted_view = models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)
