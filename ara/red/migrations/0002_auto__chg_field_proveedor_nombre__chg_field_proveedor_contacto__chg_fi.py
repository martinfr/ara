# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Proveedor.nombre'
        db.alter_column(u'red_proveedor', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Proveedor.contacto'
        db.alter_column(u'red_proveedor', 'contacto', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Proveedor.email'
        db.alter_column(u'red_proveedor', 'email', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Nodo.nombre'
        db.alter_column(u'red_nodo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Proveedor.nombre'
        db.alter_column(u'red_proveedor', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Proveedor.contacto'
        db.alter_column(u'red_proveedor', 'contacto', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Proveedor.email'
        db.alter_column(u'red_proveedor', 'email', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Nodo.nombre'
        db.alter_column(u'red_nodo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '39', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['red.Proveedor']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'red.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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