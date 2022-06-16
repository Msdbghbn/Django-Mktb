from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
def index_view(request):
    return HttpResponse("<h1> HOME PAGE </h1>")

def about_view(request):
    return HttpResponse("<h1> About PAGE </h1>")

def contact_view(request):
    return HttpResponse("<h1> Contact PAGE </h1>")
