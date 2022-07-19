import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
def login_view(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')
def signup_view(request):
    return render(request, 'accounts/signup.html')
