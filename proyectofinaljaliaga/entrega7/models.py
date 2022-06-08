from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=40)
    passw = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    isbn = models.IntegerField()
    date = models.DateField()

class Comment(models.Model):
    title= models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    date = models.DateField()

