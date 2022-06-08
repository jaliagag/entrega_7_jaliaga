#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from entrega7 import views

urlpatterns = [
  path('',views.home, name='home'),
  path('books/',views.books, name='books'),
  path('addBook/',views.home),
  path('searchBook/',views.home),
  path('authors/',views.home),
  path('addAuthor/',views.home),
  path('searchAuthor/',views.home),
  path('comments/',views.home),
  path('addComment/',views.home),
  path('searchComment/',views.home),
]
