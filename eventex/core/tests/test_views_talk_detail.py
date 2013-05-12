# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk


class TalkDetailTest(TestCase):
    def setUp(self):
        talk = Talk.objects.create(title=u'Título da Palestra', description=u'Descrição da Palestra', start_time='10:00')
        talk.speakers.create(name='Henrique Bastos', slug='henrique-bastos', url='http://henriquebastos.net')
        self.resp = self.client.get(r('core:talk_detail', kwargs={'pk': talk.pk}))
        
    def test_get(self):
        'GET deve retornar status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Template usado deve ser core/talk_detail.html'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')
        
    def test_talk_context(self):
        'Contexto deve ter uma instância de Talk'
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)
        
    def test_html(self):
        'Teste do conteúdo do html'
        self.assertContains(self.resp, u'Título da Palestra')
        self.assertContains(self.resp, '/palestrantes/henrique-bastos/')
        self.assertContains(self.resp, 'Henrique Bastos')        
        
        
class TalkDetailNotFoundTest(TestCase):
    def test_not_found(self):
        'URL inválida deve retornar status code 404'
        resp = self.client.get(r('core:talk_detail', kwargs={'pk': 0}))
        self.assertEqual(404, resp.status_code)