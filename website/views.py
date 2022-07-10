from curses.ascii import HT
from email import message
from re import sub
from django.shortcuts import render
from website.forms import NameForm
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
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            subject=form.cleaned_data['subject']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name,subject,email,message)
            return HttpResponse('done')
        else:
            return HttpResponse('error')
    form=NameForm()
    return render(request,'website2/test.html',{'form': form})
