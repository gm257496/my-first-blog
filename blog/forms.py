# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:59:35 2019

@author: gm257496
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)