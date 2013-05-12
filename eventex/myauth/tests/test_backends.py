# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()        
        UserModel.objects.create_user(username='henrique',
                                      email='henrique@bastos.net',
                                      password='abracadabra')        
        self.backend = EmailBackend()
        
    def test_authenticate_with_email(self):
        'Autenticação do usuário por e-mail'
        user = self.backend.authenticate(email='henrique@bastos.net', password='abracadabra')
        self.assertIsNotNone(user)
        
    def test_wrong_password(self):
        'Passoword incorreto deve retornar None'
        user = self.backend.authenticate(email='henrique@bastos.net', password='password')
        self.assertIsNone(user)
        
    def test_unknown_user(self):
        'Usuário não cadastrado deve retornar None'
        user = self.backend.authenticate(email='unknown@email.com', password='password')
        self.assertIsNone(user)
        
    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))
        
class MultipleEmailTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create(username='henrique',
                                 email='henrique@bastos.net',
                                 password='abracadabra')
        UserModel.objects.create(username='henrique2',
                                 email='henrique@bastos.net',
                                 password='abracadabra2')
        self.backend = EmailBackend()
        
    def test_multiple_email(self):
        'Login de e-mail duplicado deve retornar None'
        user = self.backend.authenticate(email='henrique@bastos.net', password='abracadabra')
        self.assertIsNone(user)
        
class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='henrique',
                                      email='henrique@bastos.net',
                                      password='abracadabra')
        
    def test_login_with_email(self):
        'Login com sucesso por e-mail'
        result = self.client.login(email='henrique@bastos.net', password='abracadabra')
        self.assertTrue(result)
    
    def test_login_with_username(self):
        'Login com sucesso por username'
        result = self.client.login(username='henrique@bastos.net', password='abracadabra')
        self.assertTrue(result)                 