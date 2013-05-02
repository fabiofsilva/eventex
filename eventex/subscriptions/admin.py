# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, ugettext as _
from models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'criado_em', 'subscribe_today', 'pago')
    search_fields = ('nome', 'cpf', 'telefone', 'criado_em')
    list_filter = ['criado_em', 'pago']
    date_hierarchy = 'criado_em'
    actions = ['mark_as_paid']
    
    def subscribe_today(self, obj):
        return obj.criado_em.date() == datetime.today().date()
    
    subscribe_today.short_description = _(u'Inscrito Hoje?')
    subscribe_today.boolean = True
    
    def mark_as_paid(self, request, queryset):
        count = queryset.update(pago=True)
        
        msg = ungettext(u'{0} inscrição marcada como paga.', 
                        u'{0} inscrições mardadas como pagas.', 
                        count)
        
        self.message_user(request, msg.format(count))
        
    mark_as_paid.short_description = _(u'Marcar como pago') 
    
admin.site.register(Subscription, SubscriptionAdmin)