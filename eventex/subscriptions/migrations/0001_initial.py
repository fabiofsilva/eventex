# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscription'
        db.create_table(u'subscriptions_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'subscriptions', ['Subscription'])


    def backwards(self, orm):
        # Deleting model 'Subscription'
        db.delete_table(u'subscriptions_subscription')


    models = {
        u'subscriptions.subscription': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'Subscription'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['subscriptions']