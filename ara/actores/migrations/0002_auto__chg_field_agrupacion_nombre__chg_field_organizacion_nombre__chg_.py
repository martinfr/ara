# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Agrupacion.nombre'
        db.alter_column(u'actores_agrupacion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Organizacion.nombre'
        db.alter_column(u'actores_organizacion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Atributo.nombre'
        db.alter_column(u'actores_atributo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Atributo.valor'
        db.alter_column(u'actores_atributo', 'valor', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Institucion.calle'
        db.alter_column(u'actores_institucion', 'calle', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Institucion.provincia'
        db.alter_column(u'actores_institucion', 'provincia', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Institucion.localidad'
        db.alter_column(u'actores_institucion', 'localidad', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Institucion.nombre'
        db.alter_column(u'actores_institucion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Agrupacion.nombre'
        db.alter_column(u'actores_agrupacion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Organizacion.nombre'
        db.alter_column(u'actores_organizacion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Atributo.nombre'
        db.alter_column(u'actores_atributo', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Atributo.valor'
        db.alter_column(u'actores_atributo', 'valor', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Institucion.calle'
        db.alter_column(u'actores_institucion', 'calle', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Institucion.provincia'
        db.alter_column(u'actores_institucion', 'provincia', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Institucion.localidad'
        db.alter_column(u'actores_institucion', 'localidad', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Institucion.nombre'
        db.alter_column(u'actores_institucion', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'actores.agrupacion': {
            'Meta': {'object_name': 'Agrupacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'actores.atributo': {
            'Meta': {'object_name': 'Atributo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subscripcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Subscripcion']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'actores.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'calle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'cp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'depto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Organizacion']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'piso': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'actores.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'actores.subscripcion': {
            'Meta': {'object_name': 'Subscripcion'},
            'agrupacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Agrupacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Institucion']"})
        }
    }

    complete_apps = ['actores']