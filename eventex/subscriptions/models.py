# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    nome = models.CharField(verbose_name=_(u'Nome'), max_length=100)
    cpf = models.CharField(verbose_name=_(u'CPF'), max_length=11, unique=True)
    email = models.EmailField(verbose_name=_(u'e-mail'), blank=True)
    telefone = models.CharField(verbose_name=_(u'Telefone'), max_length=20, blank=True)
    criado_em = models.DateTimeField(verbose_name=_(u'Criado em'), auto_now_add=True)
    pago = models.BooleanField(verbose_name=_(u'Pago'))
    
    class Meta:
        ordering = ['criado_em']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')
        
    def __unicode__(self):
        return self.nome
