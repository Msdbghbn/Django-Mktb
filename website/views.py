from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index_view(request):
    return render(request,'website2/index.html')

def about_view(request):
    return render(request,'website2/about.html')

def contact_view(request):
    return render(request,'website2/contact.html')

def test_view(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
    return render(request,'website2/test.html')
