# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact, Talk


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos', slug='henrique-bastos', url='http://henriquebastos.net')
        s.contact_set.add(Contact(kind='E', value='henrique@bastos.net'), 
                          Contact(kind='T', value='21-12345678'),
                          Contact(kind='F', value='21-12378945'),)
        
    def test_email(self):
        'manager deve retornar somente e-mails'
        queryset = Contact.emails.all()
        expected = ['<Contact: henrique@bastos.net>']
        self.assertQuerysetEqual(queryset, expected)
        
    def test_phone(self):
        'manager deve retornar somente telefones'
        queryset = Contact.phones.all()
        expected = ['<Contact: 21-12345678>']
        self.assertQuerysetEqual(queryset, expected)
        
    def test_faxes(self):
        'manager deve retornar somente fax'
        queryset = Contact.faxes.all()
        expected = ['<Contact: 21-12378945>']
        self.assertQuerysetEqual(queryset, expected)
        
class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='13:00')
        
    def test_at_morning(self):
        'Retorna as palestras da manhã'
        self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title)
        
    def test_at_afternoon(self):
        'Retorna as palestras da manhã'
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title)
                