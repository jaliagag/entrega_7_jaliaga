#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from entrega7 import views

urlpatterns = [
  path('',views.home, name='home'),
  path('books/',views.books, name='books'),
#  path('addbook/',views.addBook),
  path('searchbook/',views.home),
  path('authors/',views.home),
  path('addauthor/',views.home),
  path('searchauthor/',views.home),
  path('comments/',views.comments, name='comments'),
  path('addcomment/',views.home),
  path('searchcomment/',views.home),
]
