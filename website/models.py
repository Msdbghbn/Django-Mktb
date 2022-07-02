from pyexpat import model
from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    subject=models.CharField(max_length=255)
    massege=models.TextField(max_length=255)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)