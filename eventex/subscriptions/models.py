# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    nome = models.CharField(verbose_name=_(u'nome'), max_length=100)
    cpf = models.CharField(verbose_name=_(u'CPF'), max_length=11, unique=True)
    email = models.EmailField(verbose_name=_(u'e-mail'), unique=True)
    telefone = models.CharField(verbose_name=_(u'telefone'), max_length=20, blank=True)
    criado_em = models.DateTimeField(verbose_name=_(u'criado em'), auto_now_add=True)
    
    class Meta:
        ordering = ['criado_em']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')
        
    def __unicode__(self):
        return self.nome
