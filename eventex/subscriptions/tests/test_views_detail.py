# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(nome='Fabio', cpf='11111111111', email='fabio@email.com', telefone='21-12345678')
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))
        
    def test_get(self):
        'GET /inscricao/1/ should return status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Must use template subscriptions/subscription_detail.html'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')
        
    def test_context(self):
        'Context must have a Subscription instance'
        s = self.resp.context['subscription']
        self.assertIsInstance(s, Subscription)
        
    def test_html(self):
        'Check if Subscription data was rendered'
        self.assertContains(self.resp, 'Fabio')
                
class DetailNotFound(TestCase):
    def test_not_found(self):
        'URL inválida deve retornar status code 404'
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
    