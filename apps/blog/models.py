# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    """
    ブログの投稿記事
    """
    # タイトル
    title = models.CharField(
        'タイトル',
        max_length=100
    )
    # 内容
    contents = models.TextField(
        '内容'
    )
    # 公開フラグ
    is_open = models.BooleanField(
        '公開フラグ',
        default=False
    )
    # 削除フラグ
    is_deleted = models.BooleanField(
        '削除フラグ',
        default=False
    )
    # 作成日時
    record_time = models.DateTimeField(
        '作成日時',
        default=timezone.now
    )
    # 更新日時
    update_time = models.DateTimeField(
        '更新日時',
        auto_now=True,
        editable=False
    )
    # 公開日時
    open_time = models.DateTimeField(
        '公開日時',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = '投稿記事【Article】'
        db_table = 'article'
        app_label = 'blog'

    def __str__(self):
        return self.title
