# coding: utf-8:
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_forms_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['nome', 'cpf', 'email', 'telefone'], form.fields)
        
    def test_cpf_is_digit(self):
        'CPF deve aceitar apenas números'
        form = self.make_validated_form(cpf='ABC1234567')
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_cpf_has_11_digits(self):
        'CPF deve ter onze números'
        form = self.make_validated_form(cpf='123456789')
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_email_optional(self):
        'e-mail pode ser opcional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
        
    def test_name_must_be_capitalized(self):
        'Nome deve ficar capitalizado'
        form = self.make_validated_form(nome='FABIO feRreira')
        self.assertEqual('Fabio Ferreira', form.cleaned_data['nome'])
        
    def test_must_inform_email_or_phone(self):
        'e-mail ou telefone devem ser informados'
        form = self.make_validated_form(email='', telefone_0='', telefone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
    
    def make_validated_form(self, **kwargs):
        data = dict(nome='Fabio', cpf='12345678901', email='fabio@teste.com', telefone_0='21', telefone_1='12345678')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
    
    