# -*- coding: utf-8 -*-

from django.urls import path
# views
from .views import *    # noqa


# urlごとの名前空間
app_name = 'blog'
# /〜
urlpatterns = [
    # 一覧ページ（トップ）
    path('', ArticleListView.as_view(), name='article_list'),
    # 新規作成
    path('create/', ArticleCreateView.as_view(), name='article_create'),
]
