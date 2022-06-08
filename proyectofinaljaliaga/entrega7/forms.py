#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=40)
    passw = forms.CharField(max_length=40)
    email = forms.EmailField()

class BookForm(forms.Form):
    title = forms.CharField(max_length=40)
    description = forms.CharField(max_length=200)
    genre = forms.CharField(max_length=40)
    author = forms.CharField(max_length=40)
    isbn = forms.IntegerField()
    date = forms.DateField()

class CommentForm(forms.Form):
    title= forms.CharField(max_length=40)
    text = forms.CharField(max_length=200)
    date = forms.DateField()

