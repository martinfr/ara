# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organizacion'
        db.create_table(u'actores_organizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'actores', ['Organizacion'])

        # Adding model 'Institucion'
        db.create_table(u'actores_institucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('calle', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True)),
            ('cp', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('piso', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('depto', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('localidad', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
            ('ubicacion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actores.Organizacion'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'actores', ['Institucion'])

        # Adding model 'Agrupacion'
        db.create_table(u'actores_agrupacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'actores', ['Agrupacion'])

        # Adding model 'Subscripcion'
        db.create_table(u'actores_subscripcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actores.Institucion'])),
            ('agrupacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actores.Agrupacion'])),
        ))
        db.send_create_signal(u'actores', ['Subscripcion'])

        # Adding model 'Atributo'
        db.create_table(u'actores_atributo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('subscripcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actores.Subscripcion'])),
        ))
        db.send_create_signal(u'actores', ['Atributo'])


    def backwards(self, orm):
        # Deleting model 'Organizacion'
        db.delete_table(u'actores_organizacion')

        # Deleting model 'Institucion'
        db.delete_table(u'actores_institucion')

        # Deleting model 'Agrupacion'
        db.delete_table(u'actores_agrupacion')

        # Deleting model 'Subscripcion'
        db.delete_table(u'actores_subscripcion')

        # Deleting model 'Atributo'
        db.delete_table(u'actores_atributo')


    models = {
        u'actores.agrupacion': {
            'Meta': {'object_name': 'Agrupacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'actores.atributo': {
            'Meta': {'object_name': 'Atributo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'subscripcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Subscripcion']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'actores.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'calle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'depto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Organizacion']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'piso': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'actores.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'actores.subscripcion': {
            'Meta': {'object_name': 'Subscripcion'},
            'agrupacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Agrupacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Institucion']"})
        }
    }

    complete_apps = ['actores']