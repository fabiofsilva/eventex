# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Subscription', fields ['email']
        db.delete_unique(u'subscriptions_subscription', ['email'])


    def backwards(self, orm):
        # Adding unique constraint on 'Subscription', fields ['email']
        db.create_unique(u'subscriptions_subscription', ['email'])


    models = {
        u'subscriptions.subscription': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'Subscription'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pago': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['subscriptions']