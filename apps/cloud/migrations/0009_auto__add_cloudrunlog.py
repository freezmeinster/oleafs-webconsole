# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CloudRunLog'
        db.create_table(u'cloud_cloudrunlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cloud', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cloud.Cloud'])),
            ('periode', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('run_state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cloud', ['CloudRunLog'])


    def backwards(self, orm):
        # Deleting model 'CloudRunLog'
        db.delete_table(u'cloud_cloudrunlog')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cloud.addharddisk': {
            'Meta': {'object_name': 'AddHarddisk'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            'format_storage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cloud.addnetwork': {
            'Meta': {'object_name': 'AddNetwork'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'cloud.cloud': {
            'Meta': {'unique_together': "(['mac_address', 'ip_address'],)", 'object_name': 'Cloud'},
            'domain_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_created': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Node']"}),
            'os': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.OS']"}),
            'run_state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Template']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['support.CloudUser']"}),
            'vnc_port': ('django.db.models.fields.IntegerField', [], {}),
            'websocket_port': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cloud.cloudlog': {
            'Meta': {'object_name': 'CloudLog'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            'free_hdd': ('django.db.models.fields.IntegerField', [], {}),
            'free_mem': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periode': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'proc': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cloud.cloudrunlog': {
            'Meta': {'object_name': 'CloudRunLog'},
            'cloud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Cloud']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'periode': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'run_state': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.node': {
            'Meta': {'object_name': 'Node'},
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'hypervisor': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_hdd': ('django.db.models.fields.IntegerField', [], {}),
            'total_mem': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cloud.nodelog': {
            'Meta': {'object_name': 'NodeLog'},
            'free_hdd': ('django.db.models.fields.IntegerField', [], {}),
            'free_mem': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Node']"}),
            'periode': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'cloud.os': {
            'Meta': {'object_name': 'OS'},
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'base_size': ('django.db.models.fields.IntegerField', [], {}),
            'format_storage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.template': {
            'Meta': {'object_name': 'Template'},
            'asign_hdd': ('django.db.models.fields.IntegerField', [], {}),
            'asign_mem': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'support.clouduser': {
            'Meta': {'object_name': 'CloudUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['cloud']