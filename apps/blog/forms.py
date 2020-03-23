# -*- coding: utf-8 -*-

from django import forms
# SummerNote
from django_summernote.widgets import SummernoteWidget

# Model
from .models import Article


class ArticlePostForm(forms.ModelForm):
    """
    ブログの記事を投稿するフォーム
    """
    class Meta:
        model = Article
        fields = ('title', 'contents', 'is_open')
        widgets = {
            'contents': SummernoteWidget()
        }
