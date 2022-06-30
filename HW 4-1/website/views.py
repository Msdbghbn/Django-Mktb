from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

def portfolio_view(request):
    return render(request,'portfolio.html')

def testmonial_view(request):
    return render(request,'testmonial.html')

def blog_view(request):
    return render(request,'blog.html')


