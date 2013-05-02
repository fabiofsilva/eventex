# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            nome='Fabio',
            cpf='11111111111',
            email='fabio@email.com',
            telefone='21-12345678'                                
        )
    
    def test_create(self):
        'Subscription must have nome, cpf, email, telefone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
        
    def test_has_created_at(self):
        'Subscription must have automatic created at'
        self.obj.save()
        self.assertIsInstance(self.obj.criado_em, datetime)

    def test_unicode(self):
        'Unicode must be equal nome'
        self.assertEqual(u'Fabio', unicode(self.obj))
                
    def test_paid_default_value_is_False(self):
        'Pago deve ter default False'
        self.assertEqual(False, self.obj.pago)
           
class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(nome='Fabio', cpf='11111111111', email='fabio@email.com', telefone='21-12345678')
        
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(nome='Fabio', cpf='11111111111', email='outro@email.com', telefone='21-12345678')
        self.assertRaises(IntegrityError, s.save)
        
    def test_email_can_repeat(self):
        'E-mail can repeat'
        s = Subscription.objects.create(nome='Fabio', cpf='11111111112', email='fabio@email.com', telefone='21-12345678')
        self.assertEqual(2, s.pk)
        
        
        
        