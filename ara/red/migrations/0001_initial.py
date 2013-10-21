# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nodo'
        db.create_table(u'red_nodo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ubicacion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'red', ['Nodo'])

        # Adding model 'Vinculo'
        db.create_table(u'red_vinculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('recorrido', self.gf('django.contrib.gis.db.models.fields.LineStringField')()),
            ('nodo1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nodo1', null=True, on_delete=models.SET_NULL, to=orm['red.Nodo'])),
            ('nodo2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nodo2', null=True, on_delete=models.SET_NULL, to=orm['red.Nodo'])),
        ))
        db.send_create_signal(u'red', ['Vinculo'])


    def backwards(self, orm):
        # Deleting model 'Nodo'
        db.delete_table(u'red_nodo')

        # Deleting model 'Vinculo'
        db.delete_table(u'red_vinculo')


    models = {
        u'red.nodo': {
            'Meta': {'object_name': 'Nodo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'red.vinculo': {
            'Meta': {'object_name': 'Vinculo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nodo1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nodo1'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['red.Nodo']"}),
            'nodo2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nodo2'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['red.Nodo']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'recorrido': ('django.contrib.gis.db.models.fields.LineStringField', [], {})
        }
    }

    complete_apps = ['red']