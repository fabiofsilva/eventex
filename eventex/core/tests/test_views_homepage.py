# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class HomePageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))
        
    def test_get(self):
        'GET "/" must return status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Homepage must use template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
