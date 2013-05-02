# coding: utf-8
from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import Subscription, SubscriptionAdmin, admin


class MarkAsPaidTest(TestCase):
    def setUp(self):
        # Instancia o model admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        
        Subscription.objects.create(nome='Fabio', cpf='1111111111', email='fabio@email.com', telefone='21-12345678')
        
    def test_has_action(self):
        'Action instalada'
        self.assertIn('mark_as_paid', self.model_admin.actions)
        
    def test_mark_all(self):
        'Marca tudo como pago'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        self.assertEqual(1, Subscription.objects.filter(pago=True).count())