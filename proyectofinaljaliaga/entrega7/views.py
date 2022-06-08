from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    return render(request, 'entrega7/home.html')

def books(request):
    return render(request, 'entrega7/books.html')
