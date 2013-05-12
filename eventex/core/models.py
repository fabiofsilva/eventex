# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager


class Speaker(models.Model):
    name = models.CharField(verbose_name=_(u'Nome'), max_length=255)
    slug = models.SlugField(verbose_name=_(u'Slug'))
    url = models.URLField(verbose_name=_(u'URL'))
    description = models.TextField(verbose_name=_(u'Descrição'), blank=True)
    
    class Meta:
        verbose_name = _(u'Palestrante')
        verbose_name_plural = _(u'Palestrantes')
        
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})
    
class Contact(models.Model):
    KIND = (('E', _(u'e-mail')), ('F', _(u'Fax')), ('P', _(u'Telefone')),)
    
    speaker = models.ForeignKey('Speaker', verbose_name=_(u'Palestrante'))
    kind = models.CharField(verbose_name=_(u'Tipo'), max_length=1, choices=KIND)
    value = models.CharField(verbose_name=_(u'Valor'), max_length=255)
    
    objects = models.Manager()
    emails = KindContactManager(kind='E')
    faxes = KindContactManager(kind='F')
    phones = KindContactManager(kind='T')
    
    def __unicode__(self):
        return self.value
    
class Talk(models.Model):
    title = models.CharField(verbose_name=_(u'Título'), max_length=200)
    description = models.TextField(verbose_name=_(u'Descrição'))
    start_time = models.TimeField(verbose_name=_(u'Horário'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'Palestrante'))
    
    objects = PeriodManager()

    class Meta:
        verbose_name = _(u'Palestra')
        verbose_name_plural = _(u'Palestras')
            
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('core:talk_detail', (), {'pk': self.pk})
    
    @property
    def slides(self):
        return self.media_set.filter(kind='SL')
    
    @property    
    def videos(self):
        return self.media_set.filter(kind='YT')
    
class Course(Talk):
    slots = models.IntegerField(verbose_name=_(u'Slots'))
    notes = models.TextField(_(u'Notes'))
    
    objects = PeriodManager()
    
    class Meta:
        verbose_name = _(u'Curso')
        verbose_name_plural = _(u'Cursos')
        
class Media(models.Model):
    KIND = (('YT', _('YouTube')),
            ('SL', _('SlideShare')),)
    
    talk = models.ForeignKey('Talk', verbose_name=_(u'Palestra'))
    kind = models.CharField(verbose_name=_(u'Tipo'), max_length=2, choices=KIND)
    media_id = models.CharField(verbose_name=_(u'Ref'), max_length=255)
    title = models.CharField(verbose_name=_(u'Título'), max_length=200)
    
    def __unicode__(self):
        return self.talk.title + ' - ' + self.title    