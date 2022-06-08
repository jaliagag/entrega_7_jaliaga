from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from entrega7.models import *
from entrega7.forms import *

# Create your views here.

# main pages

def home(request):
    return render(request, 'entrega7/home.html')

#def books(request):
#    return render(request, 'entrega7/books.html')

def comments(request):
    return render(request, 'entrega7/comments.html')

# classes
#class UserForm(forms.Forms):
#    user_name = forms.CharField(max_length=40)
#    passw = forms.CharField(max_length=40)
#    email = forms.EmailField()
#
#class BookForm(forms.Forms):
#    title = forms.CharField(max_length=40)
#    description = forms.CharField(max_length=200)
#    genre = forms.CharField(max_length=40)
#    author = forms.CharField(max_length=40)
#    isbn = forms.IntegerField()
#    date = forms.DateField()
#
#class CommentForm(forms.Forms):
#    title= forms.CharField(max_length=40)
#    text = forms.CharField(max_length=200)
#    date = forms.DateField()


# creation pages

def books(request):
    if request.method == 'POST':
        myform = BookForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data

            title = info['title']
            description = info['description']
            genre = info['genre']
            author = info['author']
            isbn = info['isbn']
            date = info['date']

            book = Book(title=title,description=description,genre=genre,author=author,isbn=isbn,date=date)
            book.save()

            return render(request, 'entrega7/success.html')
    else:
        myform = BookForm()
    return render(request, 'entrega7/addbook.html',{'myform':myform})

# retrieving information pages

# search pages
