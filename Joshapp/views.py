from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style= 'color:brown' >My first webpage with Django</h1>")

def home(request):
    return HttpResponse("<h1 style= 'color:brown' >My Recap</h1>")




