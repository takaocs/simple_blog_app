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

    def _add_error_required(self, field, msg):
        """
        必須のエラーを追加する
        """
        v = self.cleaned_data.get(field)
        if not v:
            # 値が取得できなかった場合はエラーを追加する
            self.add_error(field, msg)

    def clean_is_open(self):
        """
        公開の場合、タイトル・内容は必須とする
        """
        is_open = self.cleaned_data.get('is_open', False)
        if is_open:
            # 公開の場合はエラーチェック
            self._add_error_required('title', 'タイトルを入力してください。')
            self._add_error_required('contents', '記事の内容を入力してください。')

        return is_open
