# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proveedor'
        db.create_table(u'red_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contacto', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
        ))
        db.send_create_signal(u'red', ['Proveedor'])

        # Adding model 'Enlace'
        db.create_table(u'red_enlace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('capacidad', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'red', ['Enlace'])

        # Adding model 'FibraOptica'
        db.create_table(u'red_fibraoptica', (
            (u'enlace_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['red.Enlace'], unique=True, primary_key=True)),
            ('hilos', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'red', ['FibraOptica'])

        # Adding model 'Nodo'
        db.create_table(u'red_nodo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['red.Proveedor'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(default='', max_length=39, blank=True)),
            ('ubicacion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'red', ['Nodo'])

        # Adding model 'Vinculo'
        db.create_table(u'red_vinculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['red.Proveedor'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('enlace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['red.Enlace'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('recorrido', self.gf('django.contrib.gis.db.models.fields.LineStringField')()),
            ('nodo1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nodo1', null=True, on_delete=models.SET_NULL, to=orm['red.Nodo'])),
            ('nodo2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nodo2', null=True, on_delete=models.SET_NULL, to=orm['red.Nodo'])),
        ))
        db.send_create_signal(u'red', ['Vinculo'])


    def backwards(self, orm):
        # Deleting model 'Proveedor'
        db.delete_table(u'red_proveedor')

        # Deleting model 'Enlace'
        db.delete_table(u'red_enlace')

        # Deleting model 'FibraOptica'
        db.delete_table(u'red_fibraoptica')

        # Deleting model 'Nodo'
        db.delete_table(u'red_nodo')

        # Deleting model 'Vinculo'
        db.delete_table(u'red_vinculo')


    models = {
        u'red.enlace': {
            'Meta': {'object_name': 'Enlace'},
            'capacidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'red.fibraoptica': {
            'Meta': {'object_name': 'FibraOptica', '_ormbases': [u'red.Enlace']},
            u'enlace_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['red.Enlace']", 'unique': 'True', 'primary_key': 'True'}),
            'hilos': ('django.db.models.fields.IntegerField', [], {})
        },
        u'red.nodo': {
            'Meta': {'object_name': 'Nodo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "''", 'max_length': '39', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['red.Proveedor']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'red.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        u'red.vinculo': {
            'Meta': {'object_name': 'Vinculo'},
            'enlace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['red.Enlace']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nodo1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nodo1'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['red.Nodo']"}),
            'nodo2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nodo2'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['red.Nodo']"}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['red.Proveedor']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'recorrido': ('django.contrib.gis.db.models.fields.LineStringField', [], {})
        }
    }

    complete_apps = ['red']