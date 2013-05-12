# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Henrique Bastos', slug='henrique-bastos',
                               url='http://henriquebastos.net', description='Passionate software developer!')
        url = r('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
        self.resp = self.client.get(url)
        
    def test_get(self):
        'GET deve retornar status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'O template deve ser core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')
        
    def test_html(self):
        'Html deve conter dados'
        self.assertContains(self.resp, 'Henrique Bastos')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://henriquebastos.net')
        
    def test_context(self):
        'Contexto deve ter o speaker'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)
        
class SpeakerNotFound(TestCase):       
    def test_not_found(self):
        'URL inválida deve retornar status code 404'
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        resp = self.client.get(url)        
        self.assertEqual(404, resp.status_code)