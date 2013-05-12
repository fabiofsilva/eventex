# coding: utf-8
from django.test import TestCase
from django.template import Context, Template


class YouTubeTagTest(TestCase):
    def setUp(self):
        context = Context({'ID': 1})
        template = Template('{% load youtube %} {% youtube ID %}')
        self.content = template.render(context)
        
    def test_output(self):
        'Teste da renderização do vídeo'
        self.assertIn('<object', self.content)
        self.assertIn('/1', self.content)
        
        
class SlideShareTest(TestCase):
    def setUp(self):
        context = Context({'ID': 1})
        template = Template('{% load slideshare %} {% slideshare ID %}')
        self.content = template.render(context)
        
    def test_output(self):
        'Teste da renderização do slide'
        self.assertIn('<iframe', self.content)
        self.assertIn('/1', self.content)
    