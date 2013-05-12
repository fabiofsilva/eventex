# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk


class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos',
                                   url='http://henriquebastos.net',
                                   description='Passionate software developer!')
        t1 = Talk.objects.create(title=u'Título da Palestra', description=u'Descrição da Palestra',
                                 start_time='10:00')
        t2 = Talk.objects.create(title=u'Título da Palestra', description=u'Descrição da Palestra',
                                 start_time='13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
                
        self.resp = self.client.get(r('core:talk_list'))
        
    def test_get(self):
        'GET deve retornar status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Template utilizado deve ser core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')
        
    def test_html(self):
        'Html deve listar as palestras'
        self.assertContains(self.resp, u'Título da Palestra', 2)
        self.assertContains(self.resp, u'/palestra/1')
        self.assertContains(self.resp, u'/palestra/2')
        self.assertContains(self.resp, u'/palestrantes/henrique-bastos', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Henrique Bastos', 2)
        self.assertContains(self.resp, u'Descrição da Palestra', 2)
        
    def test_morning_talk_context(self):
        'Contexto deve ter morning_talks'
        self.assertIn('morning_talks', self.resp.context)
        
    def test_afternoon_talk_context(self):
        'Contexto deve ter afternoon_talks'
        self.assertIn('afternoon_talks', self.resp.context)        