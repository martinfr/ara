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
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'actores', ['Organizacion'])

        # Adding model 'Institucion'
        db.create_table(u'actores_institucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('ubicacion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actores.Organizacion'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'actores', ['Institucion'])

        # Adding model 'Agrupacion'
        db.create_table(u'actores_agrupacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'actores', ['Agrupacion'])

        # Adding M2M table for field instituciones on 'Agrupacion'
        m2m_table_name = db.shorten_name(u'actores_agrupacion_instituciones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agrupacion', models.ForeignKey(orm[u'actores.agrupacion'], null=False)),
            ('institucion', models.ForeignKey(orm[u'actores.institucion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agrupacion_id', 'institucion_id'])


    def backwards(self, orm):
        # Deleting model 'Organizacion'
        db.delete_table(u'actores_organizacion')

        # Deleting model 'Institucion'
        db.delete_table(u'actores_institucion')

        # Deleting model 'Agrupacion'
        db.delete_table(u'actores_agrupacion')

        # Removing M2M table for field instituciones on 'Agrupacion'
        db.delete_table(db.shorten_name(u'actores_agrupacion_instituciones'))


    models = {
        u'actores.agrupacion': {
            'Meta': {'object_name': 'Agrupacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituciones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['actores.Institucion']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'actores.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actores.Organizacion']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'ubicacion': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'actores.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['actores']