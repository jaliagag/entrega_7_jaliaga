from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#my_template = loader.get_template('index.html')

#def home(request):
#  return HttpResponse('Hola django-coder')

def home(self):
    template = loader.get_template('index.html')
    document = template.render()
    
    #return HttpResponse(request, 'entrega7/inicio.html')
    return HttpResponse(document)

