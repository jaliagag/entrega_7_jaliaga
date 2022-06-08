#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from entrega7 import views

urlpatterns = [
  path('',views.home),
]
