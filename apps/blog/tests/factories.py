# -*- coding: utf-8 -*-

import factory

# Models
from ..models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    """
    ブログの投稿記事のテストモデル
    """
    class Meta:
        model = Article
