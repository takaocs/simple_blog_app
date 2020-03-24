# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Apps
from .models import Article
from .forms import ArticlePostForm

# Summer Noteに関連するモジュール
from django_summernote.views import (
    SummernoteEditor as BaseSummernoteEditor,
    SummernoteUploadAttachment as BaseSummernoteUploadAttachment
)
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.


class ArticleListView(ListView):
    """
    一覧ページ
    """
    # クエリセット
    queryset = Article.objects.filter(is_deleted=False)
    # テンプレート
    template_name = 'blog/article_list.html'


class ArticleCreateView(CreateView):
    """
    新規作成
    """
    # フォームクラス
    form_class = ArticlePostForm
    # 登録後のリダイレクト先
    success_url = reverse_lazy('blog:article_list')
    # テンプレート
    template_name = 'blog/article_create.html'


class SummernoteEditor(BaseSummernoteEditor):
    """
    Summer Noteのみiframeを許可する
    """
    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SummernoteUploadAttachment(BaseSummernoteUploadAttachment):
    """
    Summer Noteのみiframeを許可する
    """
    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
