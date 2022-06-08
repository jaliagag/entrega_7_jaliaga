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
def searchthecomment(request):
    if request.GET['title']:
        title = request.GET['title']
        titles = Comment.objects.filter(title__icontains=title)

        return render(request, 'entrega7/commentresults.html',{'titles':titles,'title':title})

    else:
        respon = 'no se enviaron datos'
    return HttpResponse(respon)
############################

def users(request):
    return render(request,'entrega7/users.html')

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

def searchtheuser(request):
    if request.GET['user_name']:
        user_name = request.GET['user_name']
        users = User.objects.filter(user_name__icontains=user_name)

        return render(request, 'entrega7/userresults.html',{'users':users,'user_name':user_name})

    else:
        respon = 'no se enviaron datos'
    return HttpResponse(respon)

def searchuser(request):
    return render(request,'entrega7/searchuser.html')

########################
def books(request):
    return render(request,'entrega7/books.html')

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

def searchthebook(request):
    #if request.GET.get('author'):
    if request.GET['author']:
        author = request.GET['author']
        books = Book.objects.filter(author__icontains=author)

        return render(request, 'entrega7/bookresults.html',{'books':books,'author':author})

    else:
        respon = 'no se enviaron datos'
    return HttpResponse(respon)

def searchbook(request): # busquedacamada
    return render(request,'entrega7/searchbook.html')

#def bookresults(request):
#    #
#    return render(request,'entrega7/bookresults.html')
