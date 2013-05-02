# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))
        
    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Must use template subscriptions/subscription_form.html'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_html(self):
        'Html must contains input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')
        
    def test_csrf(self):
        'Html must contains csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        
    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        
class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(nome='Fabio', cpf='11111111111', email='fabio@email.com', telefone='21-12345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)
        
    def test_post(self):
        'Valid POST must return status_code 302'
        self.assertEqual(302, self.resp.status_code)
        
    def test_save(self):
        'Valid POST must saved'
        self.assertTrue(Subscription.objects.exists())
        
class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(nome='Fabio', cpf='000000000012', email='fabio@email.com', telefone='21-12345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)
        
    def test_post(self):
        'Invalid POST /inscricao/ should return status code 200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_form_errors(self):
        'Form must contains errors'
        self.assertTrue(self.resp.context['form'].errors)
        
    def test_dont_save(self):
        'Dont save data'
        self.assertFalse(Subscription.objects.exists())
        
class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(nome='Fabio', cpf='12345678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<ul class="errorlist">')   