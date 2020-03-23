# -*- coding: utf-8 -*-

from django.test import TestCase

# Apps
from ..forms import ArticlePostForm

# Create your tests here.


class ArticlePostFormTestCase(TestCase):
    """
    ブログの記事を投稿するフォームのテスト
    """
    def test_article_temporarily_saved(self):
        """
        一時保存の状態で登録
        """
        ...
