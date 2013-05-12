# coding: utf-8
from django import forms
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext as _
from models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise forms.ValidationError(_(u'CPF deve conter apenas números.'))
    
    if len(value) != 11:
        raise forms.ValidationError(_(u'CPF deve conter 11 números.'))

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.TextInput(attrs=dict(max_length=2, size=2)),
                   forms.TextInput(attrs=dict(max_length=9, size=9)))        
        super(PhoneWidget, self).__init__(widgets, attrs=attrs)
        
    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')
        
class PhoneField(forms.MultiValueField):
    widget = PhoneWidget
    
    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(), 
                  forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)
    
    def compress(self, data_list):
        if not data_list:
            return ''
        
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido.'))
        
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido.'))
        
        return '{0}-{1}'.format(*data_list)
        
class SubscriptionForm(forms.ModelForm):
    telefone = PhoneField(label=_(u'Telefone'), required=False)
    
    class Meta:
        model = Subscription
        fields = ('nome', 'cpf', 'email', 'telefone', )
        
    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        
        self.fields['cpf'].validators.append(CPFValidator)
        
    def clean_nome(self):
        name = self.cleaned_data['nome']
        words = map(lambda w: w.capitalize(), name.split())            
        capitalized_name = ' '.join(words)
        return capitalized_name
    
    def clean(self):
        super(SubscriptionForm, self).clean()
       
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('telefone'):
            raise forms.ValidationError(_(u'Informe seu e-mail ou telefone.'))
        
        return self.cleaned_data