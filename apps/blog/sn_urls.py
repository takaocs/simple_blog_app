# -*- coding: utf-8 -*-

from django.urls import path
# views
from .views import *


# app_nameを設定するとエラーになる
urlpatterns = [
    path(
        'editor/<str:id>/',
        SummernoteEditor.as_view(),
        name='django_summernote-editor'
    ),
    path(
        'upload_attachment/',
        SummernoteUploadAttachment.as_view(),
        name='django_summernote-upload_attachment'
    ),
]
