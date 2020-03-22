# -*- coding: utf-8 -*-

from django.test import TestCase

# Factories
from .factories import ArticleFactory

# Create your tests here.


class ArticleTestCase(TestCase):
    """
    ブログの投稿記事モデルのテスト
    """
    def test_str(self):
        """
        出力のテスト
        """
        # インスタンスの取得
        article = ArticleFactory(title='ブログの記事のタイトル')
        # 出力が登録されたタイトルか確認
        self.assertEqual(str(article), 'ブログの記事のタイトル')
