from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=40)
    passw = models.CharField(max_length=40)
    email = models.EmailField()
    def __srt__(self) -> str:
        return self.user_name+' '+str(self.passw)+' '+str(self.email)


class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    isbn = models.IntegerField()
    date = models.DateField()

    def __srt__(self) -> str:
        return self.title+' '+str(self.description)+' '+str(self.genre)+' '+str(self.author)+' '+str(self.isbn)+' '+str(self.date)

class Comment(models.Model):
    title= models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    date = models.DateField()

    def __srt__(self) -> str:
        return self.title+' '+str(self.text)+' '+str(self.date)

