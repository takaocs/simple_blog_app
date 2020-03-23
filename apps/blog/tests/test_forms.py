# -*- coding: utf-8 -*-

from django.test import TestCase

# Apps
from ..forms import ArticlePostForm

# Create your tests here.


class ArticlePostFormTestCase(TestCase):
    """
    ブログの記事を投稿するフォームのテスト

    - 一時保存（is_open が False）の場合
        - タイトルが未入力でも登録できるかどうか
        - 内容が未入力でも登録できるかどうか
    - 公開（is_open が True）の場合
        - タイトルが未入力だとエラーになるかどうか
        - 内容が未入力だとエラーになるかどうか
        - 公開日時に現在時刻が登録されるかどうか
    """
    def test_is_open_false_title_not_required(self):
        """
        一時保存の場合、タイトルが未入力でも登録できるかどうか
        """
        form = ArticlePostForm(
            data={
                'contents': 'テスト',
                'is_open': False
            }
        )
        self.assertTrue(form.is_valid())

    def test_is_open_false_contents_not_required(self):
        """
        一時保存の場合、内容が未入力でも登録できるかどうか
        """
        form = ArticlePostForm(
            data={
                'title': 'テスト',
                'is_open': False
            }
        )
        self.assertTrue(form.is_valid())

    def test_is_open_true_title_required(self):
        """
        公開の場合、タイトルが未入力の場合エラーとなる
        """
        form = ArticlePostForm(
            data={
                'contents': 'テスト',
                'is_open': True
            }
        )

        # バリデーションの確認
        self.assertFalse(form.is_valid())
        # エラーメッセージも確認
        elf.assertEqual(form.errors['title'][0], 'タイトルを入力してください。')

    def test_is_open_true_contents_required(self):
        """
        公開の場合、内容が未入力の場合エラーとなる
        """
        form = ArticlePostForm(
            data={
                'title': 'テスト',
                'is_open': True
            }
        )

        # バリデーションの確認
        self.assertFalse(form.is_valid())
        # エラーメッセージも確認
        elf.assertEqual(form.errors['contents'][0], '記事の内容を入力してください。')
