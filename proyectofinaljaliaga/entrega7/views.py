from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from entrega7.models import *
from entrega7.forms import *

# Create your views here.

# main pages

def home(request):
    return render(request, 'entrega7/home.html')

############################

def comments(request):
    return render(request,'entrega7/comments.html')

def searchcomment(request):
    return render(request,'entrega7/searchcomment.html')

def addcomment(request):
    if request.method == 'POST':
        myform = CommentForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data

            title = info['title']
            text = info['text']
            date = info['date']

            comment = Comment(title=title,text=text,date=date)
            comment.save()

            return render(request, 'entrega7/success.html')
    else:
        myform = CommentForm()
    return render(request, 'entrega7/addcomment.html',{'myform':myform})

############################

def users(request):
    return render(request,'entrega7/users.html')

def searchuser(request):
    return render(request,'entrega7/searchuser.html')

def adduser(request):
    if request.method == 'POST':
        myform = UserForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data

            user_name = info['user_name']
            passw = info['passw']
            email = info['email']

            user = User(user_name=user_name,passw=passw,email=email)
            user.save()

            return render(request, 'entrega7/success.html')
    else:
        myform = UserForm()
    return render(request, 'entrega7/adduser.html',{'myform':myform})

########################

def addbook(request):
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
            user = info['user']

            book = Book(title=title,description=description,genre=genre,author=author,isbn=isbn,date=date,user=user)
            book.save()

            return render(request, 'entrega7/success.html')
    else:
        myform = BookForm()
    return render(request, 'entrega7/addbook.html',{'myform':myform})

def books(request):
    return render(request,'entrega7/books.html')

def searchbook(request):
    # search logic
    return render(request,'entrega7/searchbook.html')

# retrieving information pages

# search pages
