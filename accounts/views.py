import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
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
    return render(request, 'accounts/signup.html')