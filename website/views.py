from curses.ascii import HT
from email import message
from re import sub
from django.shortcuts import render
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from website.models import Newsletter
def index_view(request):
    return render(request,'website2/index.html')

def about_view(request):
    return render(request,'website2/about.html')

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():

            form.save()
            messages.add_message(request,messages.SUCCESS,'Successfully created')
            
        else:
            messages.add_message(request,messages.ERROR,' Wrong Input ')
    form=ContactForm()
    return render(request,'website2/contact.html',{'form': form})

def test_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('error')
    form=ContactForm()
    return render(request,'website2/test.html',{'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

