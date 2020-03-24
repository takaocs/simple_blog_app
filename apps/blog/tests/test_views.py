# -*- coding: utf-8 -*-

from django.test import TestCase, RequestFactory

# Apps
from ..views import SummernoteEditor, SummernoteUploadAttachment


class SummernoteEditorTestCase(TestCase):
    """
    iframeを許可する
    """
    def test_x_frame_options(self):
        """
        X-Frame-OptionsがSAMEORIGINになっているかどうか
        """
        # リクエストを取得
        request = RequestFactory().get('summernote/editor/1/')
        # レスポンスを取得
        response = SummernoteEditor.as_view()(request, id='1')
        # 確認
        self.assertEqual(response['X-Frame-Options'], 'SAMEORIGIN')


class SummernoteUploadAttachmentTestCase(TestCase):
    """
    iframeを許可する
    """
    def test_x_frame_options(self):
        """
        X-Frame-OptionsがSAMEORIGINになっているかどうか
        """
        # リクエストを取得
        request = RequestFactory().get('summernote/upload_attachment/')
        # レスポンスを取得
        response = SummernoteUploadAttachment.as_view()(request)
        # 確認
        self.assertEqual(response['X-Frame-Options'], 'SAMEORIGIN')
