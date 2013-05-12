# coding: utf-8
from django.test import TestCase
from django.core.validators import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.obj = Speaker.objects.create(name='Henrique Bastos', 
                                          url='http://henriquebastos.net',
                                          description='Passionate software developer!',
                                          slug='henrique-bastos')
        
    def test_create(self):
        'Deve criar um registro'
        self.assertEqual(1, self.obj.pk)
        
    def test_unicode(self):
        'Unicode deve ser igual ao nome'
        self.assertEqual(u'Henrique Bastos', unicode(self.obj))
        
class ContatModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Henrique Bastos', 
                                              url='http://henriquebastos.net',
                                              description='Passionate software developer!',
                                              slug='henrique-bastos')
        
    def test_email(self):
        'Criação do e-mail'
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.assertEqual(1, contact.pk)
        
    def test_phone(self):
        'Criação do telefone'
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='21-12345678')
        self.assertEqual(1, contact.pk)
        
    def test_fax(self):
        'Criação do fax'
        contact = Contact.objects.create(speaker=self.speaker, kind='F', value='21-27456123')
        self.assertEqual(1, contact.pk)
        
    def test_kind(self):
        'Deve criar kind "E", "F" e "P"'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)
        
    def test_unicode(self):
        'Unicode deve ser igual ao value'
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.assertEqual(u'henrique@bastos.net', unicode(contact))
        
            