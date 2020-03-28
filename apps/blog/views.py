# -*- coding: utf-8 -*-

from django.views.generic import CreateView
from django.urls import reverse_lazy

# django_filter
from django_filters.views import FilterView

# Apps
from .models import Article
from .forms import ArticlePostForm
from .filters import ArticleFilter

# Summer Noteに関連するモジュール
from django_summernote.views import (
    SummernoteEditor as BaseSummernoteEditor,
    SummernoteUploadAttachment as BaseSummernoteUploadAttachment
)
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.


class ArticleListView(FilterView):
    """
    一覧ページ
    """
    # フィルターセット
    filterset_class = ArticleFilter
    # クエリセット
    queryset = Article.objects.filter(is_deleted=False)
    # 10件で1ページとする
    paginate_by = 1
    # 並び替えの設定
    ordering = '-id'
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
