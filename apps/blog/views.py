# -*- coding: utf-8 -*-

from django.views.generic import ListView

# Models
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    """
    一覧ページ
    """
    # クエリセット
    queryset = Article.objects.filter(is_deleted=False)
    # テンプレート
    template_name = 'blog/article_list.html'
