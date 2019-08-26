# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:16:05 2019

@author: gm257496
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]