# -*- coding: utf-8 -*-

import django_filters

# キーワード検索関連
import operator
from functools import reduce
from django.db.models import Q

# Models
from .models import Article


class ArticleFilter(django_filters.FilterSet):
    """
    投稿記事の検索
    """
    # キーワード検索
    q = django_filters.CharFilter(
        label='検索',
        method='search_keyword'
    )
    # 公開・一時保存の切り替え
    is_open = django_filters.ChoiceFilter(
        choices=(
            (True, '公開'),
            (False, '一時保存')
        ),
        empty_label='-------'
    )
    # 並び替え
    o = django_filters.OrderingFilter(
        fields=(
            ('open_time', 'open'),
            ('record_time', 'record'),
        ),
        choices=(
            ('open', '公開日時順'),
            ('record', '作成日時順'),
        )
    )

    class Meta:
        model = Article
        fields = []

    def search_keyword(self, queryset, name, value):
        """
        検索処理
        """
        # キーワード検索対象のフィールド
        targets = ['title', 'contents']
        # 対象のフィールドを部分一致に変換
        orm_lookups = [f'{t}__icontains' for t in targets]
        # キーワードをリストに変換
        search_term = value.split()

        for bit in search_term:
            # 1キーワードずつ処理して、条件を生成
            or_queries = [Q(**{orm_lookup: bit}) for orm_lookup in orm_lookups]
            # 検索
            queryset = queryset.filter(reduce(operator.or_, or_queries))

        return queryset
