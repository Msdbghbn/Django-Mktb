import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def login_view(request):
    if not request.user.is_authenticated:
        form=AuthenticationForm(request=request,data=request.GET)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        form=AuthenticationForm()
        context={'form': form}
        return render(request, 'accounts/login.html',context)
    else:
        return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        #if request.method == 'POST':
        form=UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = UserCreationForm()
        context={'form': form}
        return render(request, 'accounts/signup.html',context)
    else:
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return redirect('/')