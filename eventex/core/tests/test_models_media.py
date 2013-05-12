# coding: utf-8
from django.test import TestCase
from eventex.core.models import Media, Talk


class MediaModelTest(TestCase):
    def setUp(self):
        talk = Talk.objects.create(title=u'Talk', start_time='10:00')
        self.media = Media.objects.create(talk=talk, kind='YT', media_id='QjA5faZF1A8', title=u'Vídeo')
        
    def test_create(self):
        'Deve criar um registro'
        self.assertEqual(1, self.media.pk)
        
    def test_unicode(self):
        'Unicode deve ser talk.title + media.title'
        self.assertEqual(u'Talk - Vídeo', unicode(self.media))        