# -*- coding: utf-8 -*-

from django.test import TestCase

# Factories
from .factories import ArticleFactory
# Apps
from ..filters import ArticleFilter
from ..models import Article


class ArticleFilterTestCase(TestCase):
    """
    投稿記事の検索のテスト
    """
    def setUp(self):
        """ 初期設定 """
        ArticleFactory(title='こんにちは', contents='とても良い天気です。', is_open=True)
        ArticleFactory(title='ご報告', contents='本日をもって退社いたしました。', is_open=False)
        ArticleFactory(title='明日の天気', contents='明日は晴れるみたいなので、出かけたいと思います。', is_open=True)

        # 登録された投稿記事全て（削除は除く）
        self.articles = Article.objects.filter(is_deleted=False)

    def test_search_keyword(self):
        """
        キーワードの検索
        """
        f = ArticleFilter({'q': '天気'}, self.articles)
        # 2件取得されるはず
        self.assertEqual(f.qs.count(), 2)

    def test_search_select_is_open_true(self):
        """
        公開・一時保存の検索
        """
        f = ArticleFilter({'is_open': True}, self.articles)
        # 2件取得されるはず
        self.assertEqual(f.qs.count(), 2)

    def test_search_select_is_open_false(self):
        """
        公開・一時保存の検索
        """
        f = ArticleFilter({'is_open': False}, self.articles)
        # 1件取得されるはず
        self.assertEqual(f.qs.count(), 1)

    def test_ordering_record_time(self):
        """
        作成日時順の並び替え
        """
        f = ArticleFilter({'o': 'record'}, self.articles)
        # IDが3のはず
        self.assertEqual(f.qs.first().id, 3)

    # def test_form_field_count(self):
    #     """
    #     フィールドの数を確認
    #     """
    #     f = ArticleFilter({'q': 'テスト'}, self.articles)

    #     print(f.form.fields['o'].widget.render('o', 'record'))
    #     self.assertHTMLEqual(
    #         f.form.fields['o'].widget.render('o', True),
    #         """
    #         <select name="is_open">
    #             <option value="">-------</option>
    #             <option value="True" selected>公開</option>
    #             <option value="False">一時保存</option>
    #         </select>
    #         """
    #     )
