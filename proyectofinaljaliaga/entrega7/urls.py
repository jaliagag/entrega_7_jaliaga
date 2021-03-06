#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from entrega7 import views

urlpatterns = [
  path('',views.home, name='home'),

  path('books/',views.books, name='books'), #
  path('addbook/',views.addbook, name='addbook'), # 
  path('searchbook/',views.searchbook, name='searchbook'), #
  path('bookresults/',views.searchthebook,name='searchthebook'),

  path('users/',views.users, name='users'), # 
  path('adduser/',views.adduser, name='adduser'),
  path('searchuser/',views.searchuser, name='searchuser'),
  path('userresults/',views.searchtheuser,name='searchtheuser'),

  path('comments/',views.comments, name='comments'), # 
  path('addcomment/',views.addcomment, name='addcomment'),
  path('searchcomment/',views.searchcomment, name='searchcomment'),
  path('commentresults/',views.searchthecomment,name='searchthecomment'),

]
