# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'cloud_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cloud', ['Node'])

        # Adding model 'NodeLog'
        db.create_table(u'cloud_nodelog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cloud.Node'])),
        ))
        db.send_create_signal(u'cloud', ['NodeLog'])

        # Adding model 'OS'
        db.create_table(u'cloud_os', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cloud', ['OS'])

        # Adding model 'Template'
        db.create_table(u'cloud_template', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cloud', ['Template'])

        # Adding model 'Cloud'
        db.create_table(u'cloud_cloud', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cloud', ['Cloud'])

        # Adding model 'CloudLog'
        db.create_table(u'cloud_cloudlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cloud', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cloud.Cloud'])),
        ))
        db.send_create_signal(u'cloud', ['CloudLog'])

        # Adding model 'AddHarddisk'
        db.create_table(u'cloud_addharddisk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cloud', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cloud.Cloud'])),
        ))
        db.send_create_signal(u'cloud', ['AddHarddisk'])

        # Adding model 'AddNetwork'
        db.create_table(u'cloud_addnetwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cloud', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cloud.Cloud'])),
        ))
        db.send_create_signal(u'cloud', ['AddNetwork'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'cloud_node')

        # Deleting model 'NodeLog'
        db.delete_table(u'cloud_nodelog')

        # Deleting model 'OS'
        db.delete_table(u'cloud_os')

        # Deleting model 'Template'
        db.delete_table(u'cloud_template')

        # Deleting model 'Cloud'
        db.delete_table(u'cloud_cloud')

        # Deleting model 'CloudLog'
        db.delete_table(u'cloud_cloudlog')

        # Deleting model 'AddHarddisk'
        db.delete_table(u'cloud_addharddisk')

        # Deleting model 'AddNetwork'
        db.delete_table(u'cloud_addnetwork')


    models = {
        u'cloud.addharddisk': {
            'Meta': {'object_name': 'AddHarddisk'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cloud.addnetwork': {
            'Meta': {'object_name': 'AddNetwork'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cloud.cloud': {
            'Meta': {'object_name': 'Cloud'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.cloudlog': {
            'Meta': {'object_name': 'CloudLog'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cloud.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.nodelog': {
            'Meta': {'object_name': 'NodeLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Node']"})
        },
        u'cloud.os': {
            'Meta': {'object_name': 'OS'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.template': {
            'Meta': {'object_name': 'Template'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cloud']