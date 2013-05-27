# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NodeLog.free_mem'
        db.add_column(u'cloud_nodelog', 'free_mem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'NodeLog.free_hdd'
        db.add_column(u'cloud_nodelog', 'free_hdd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'NodeLog.periode'
        db.add_column(u'cloud_nodelog', 'periode',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 5, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'CloudLog.free_mem'
        db.add_column(u'cloud_cloudlog', 'free_mem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'CloudLog.free_hdd'
        db.add_column(u'cloud_cloudlog', 'free_hdd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'CloudLog.proc'
        db.add_column(u'cloud_cloudlog', 'proc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'CloudLog.periode'
        db.add_column(u'cloud_cloudlog', 'periode',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 5, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OS.password'
        db.add_column(u'cloud_os', 'password',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'OS.base_size'
        db.add_column(u'cloud_os', 'base_size',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'OS.format_storage'
        db.add_column(u'cloud_os', 'format_storage',
                      self.gf('django.db.models.fields.CharField')(default='raw', max_length=20),
                      keep_default=False)

        # Adding field 'OS.path'
        db.add_column(u'cloud_os', 'path',
                      self.gf('django.db.models.fields.CharField')(default='/var/tenriolacloud/templates/', max_length=255),
                      keep_default=False)

        # Adding field 'OS.is_active'
        db.add_column(u'cloud_os', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'AddNetwork.mac_address'
        db.add_column(u'cloud_addnetwork', 'mac_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'AddNetwork.ip_address'
        db.add_column(u'cloud_addnetwork', 'ip_address',
                      self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', max_length=15),
                      keep_default=False)

        # Adding field 'AddNetwork.is_active'
        db.add_column(u'cloud_addnetwork', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'AddHarddisk.size'
        db.add_column(u'cloud_addharddisk', 'size',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'AddHarddisk.format_storage'
        db.add_column(u'cloud_addharddisk', 'format_storage',
                      self.gf('django.db.models.fields.CharField')(default='raw', max_length=20),
                      keep_default=False)

        # Adding field 'AddHarddisk.path'
        db.add_column(u'cloud_addharddisk', 'path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'AddHarddisk.is_active'
        db.add_column(u'cloud_addharddisk', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Cloud.mac_address'
        db.add_column(u'cloud_cloud', 'mac_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Cloud.ip_address'
        db.add_column(u'cloud_cloud', 'ip_address',
                      self.gf('django.db.models.fields.IPAddressField')(default='', max_length=15),
                      keep_default=False)

        # Adding field 'Cloud.node'
        db.add_column(u'cloud_cloud', 'node',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cloud.Node']),
                      keep_default=False)

        # Adding field 'Cloud.template'
        db.add_column(u'cloud_cloud', 'template',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cloud.Template']),
                      keep_default=False)

        # Adding field 'Cloud.os'
        db.add_column(u'cloud_cloud', 'os',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cloud.OS']),
                      keep_default=False)

        # Adding field 'Cloud.user'
        db.add_column(u'cloud_cloud', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['support.CloudUser']),
                      keep_default=False)

        # Adding field 'Cloud.is_active'
        db.add_column(u'cloud_cloud', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Node.total_mem'
        db.add_column(u'cloud_node', 'total_mem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.total_hdd'
        db.add_column(u'cloud_node', 'total_hdd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Node.ip_address'
        db.add_column(u'cloud_node', 'ip_address',
                      self.gf('django.db.models.fields.IPAddressField')(default='', max_length=15),
                      keep_default=False)

        # Adding field 'Node.is_active'
        db.add_column(u'cloud_node', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Template.asign_mem'
        db.add_column(u'cloud_template', 'asign_mem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Template.asign_hdd'
        db.add_column(u'cloud_template', 'asign_hdd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Template.is_active'
        db.add_column(u'cloud_template', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NodeLog.free_mem'
        db.delete_column(u'cloud_nodelog', 'free_mem')

        # Deleting field 'NodeLog.free_hdd'
        db.delete_column(u'cloud_nodelog', 'free_hdd')

        # Deleting field 'NodeLog.periode'
        db.delete_column(u'cloud_nodelog', 'periode')

        # Deleting field 'CloudLog.free_mem'
        db.delete_column(u'cloud_cloudlog', 'free_mem')

        # Deleting field 'CloudLog.free_hdd'
        db.delete_column(u'cloud_cloudlog', 'free_hdd')

        # Deleting field 'CloudLog.proc'
        db.delete_column(u'cloud_cloudlog', 'proc')

        # Deleting field 'CloudLog.periode'
        db.delete_column(u'cloud_cloudlog', 'periode')

        # Deleting field 'OS.password'
        db.delete_column(u'cloud_os', 'password')

        # Deleting field 'OS.base_size'
        db.delete_column(u'cloud_os', 'base_size')

        # Deleting field 'OS.format_storage'
        db.delete_column(u'cloud_os', 'format_storage')

        # Deleting field 'OS.path'
        db.delete_column(u'cloud_os', 'path')

        # Deleting field 'OS.is_active'
        db.delete_column(u'cloud_os', 'is_active')

        # Deleting field 'AddNetwork.mac_address'
        db.delete_column(u'cloud_addnetwork', 'mac_address')

        # Deleting field 'AddNetwork.ip_address'
        db.delete_column(u'cloud_addnetwork', 'ip_address')

        # Deleting field 'AddNetwork.is_active'
        db.delete_column(u'cloud_addnetwork', 'is_active')

        # Deleting field 'AddHarddisk.size'
        db.delete_column(u'cloud_addharddisk', 'size')

        # Deleting field 'AddHarddisk.format_storage'
        db.delete_column(u'cloud_addharddisk', 'format_storage')

        # Deleting field 'AddHarddisk.path'
        db.delete_column(u'cloud_addharddisk', 'path')

        # Deleting field 'AddHarddisk.is_active'
        db.delete_column(u'cloud_addharddisk', 'is_active')

        # Deleting field 'Cloud.mac_address'
        db.delete_column(u'cloud_cloud', 'mac_address')

        # Deleting field 'Cloud.ip_address'
        db.delete_column(u'cloud_cloud', 'ip_address')

        # Deleting field 'Cloud.node'
        db.delete_column(u'cloud_cloud', 'node_id')

        # Deleting field 'Cloud.template'
        db.delete_column(u'cloud_cloud', 'template_id')

        # Deleting field 'Cloud.os'
        db.delete_column(u'cloud_cloud', 'os_id')

        # Deleting field 'Cloud.user'
        db.delete_column(u'cloud_cloud', 'user_id')

        # Deleting field 'Cloud.is_active'
        db.delete_column(u'cloud_cloud', 'is_active')

        # Deleting field 'Node.total_mem'
        db.delete_column(u'cloud_node', 'total_mem')

        # Deleting field 'Node.total_hdd'
        db.delete_column(u'cloud_node', 'total_hdd')

        # Deleting field 'Node.ip_address'
        db.delete_column(u'cloud_node', 'ip_address')

        # Deleting field 'Node.is_active'
        db.delete_column(u'cloud_node', 'is_active')

        # Deleting field 'Template.asign_mem'
        db.delete_column(u'cloud_template', 'asign_mem')

        # Deleting field 'Template.asign_hdd'
        db.delete_column(u'cloud_template', 'asign_hdd')

        # Deleting field 'Template.is_active'
        db.delete_column(u'cloud_template', 'is_active')


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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'Meta': {'object_name': 'Cloud'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Node']"}),
            'os': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.OS']"}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cloud.Template']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['support.CloudUser']"})
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
        u'cloud.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'base_size': ('django.db.models.fields.IntegerField', [], {}),
            'format_storage': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cloud.template': {
            'Meta': {'object_name': 'Template'},
            'asign_hdd': ('django.db.models.fields.IntegerField', [], {}),
            'asign_mem': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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