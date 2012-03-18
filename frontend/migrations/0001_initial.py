# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AdFormat'
        db.create_table(u'ad_formats', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ad_format_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('frontend', ['AdFormat'])

        # Adding model 'Network'
        db.create_table(u'networks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('network_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pay_type', self.gf('django.db.models.fields.CharField')(default='Per Impression', max_length=255)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('supports_threshold', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('us_only', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contact_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('billing_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('reporting_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('frontend', ['Network'])

        # Adding model 'NetworkTagOption'
        db.create_table(u'network_tag_options', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Network'])),
            ('option_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('frontend', ['NetworkTagOption'])

        # Adding model 'Publisher'
        db.create_table(u'publishers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('site_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('hoptime', self.gf('django.db.models.fields.IntegerField')(default=1500, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('site_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('frontend', ['Publisher'])

        # Adding model 'Tag'
        db.create_table(u'tags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Network'])),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Publisher'])),
            ('value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('always_fill', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sample_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('tier', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('frequency_cap', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rejection_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('floor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('max_daily_impressions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pacing', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('frontend', ['Tag'])

        # Adding model 'TagOption'
        db.create_table(u'tag_options', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tag'])),
            ('option_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('option_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('frontend', ['TagOption'])

        # Adding model 'TagTarget'
        db.create_table(u'tag_targets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Tag'])),
            ('key_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('key_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('frontend', ['TagTarget'])


    def backwards(self, orm):
        
        # Deleting model 'AdFormat'
        db.delete_table(u'ad_formats')

        # Deleting model 'Network'
        db.delete_table(u'networks')

        # Deleting model 'NetworkTagOption'
        db.delete_table(u'network_tag_options')

        # Deleting model 'Publisher'
        db.delete_table(u'publishers')

        # Deleting model 'Tag'
        db.delete_table(u'tags')

        # Deleting model 'TagOption'
        db.delete_table(u'tag_options')

        # Deleting model 'TagTarget'
        db.delete_table(u'tag_targets')


    models = {
        'frontend.adformat': {
            'Meta': {'object_name': 'AdFormat', 'db_table': "u'ad_formats'"},
            'ad_format_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'frontend.network': {
            'Meta': {'object_name': 'Network', 'db_table': "u'networks'"},
            'billing_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'default': "'Per Impression'", 'max_length': '255'}),
            'reporting_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'supports_threshold': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'us_only': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'frontend.networktagoption': {
            'Meta': {'object_name': 'NetworkTagOption', 'db_table': "u'network_tag_options'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Network']"}),
            'option_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'frontend.publisher': {
            'Meta': {'object_name': 'Publisher', 'db_table': "u'publishers'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hoptime': ('django.db.models.fields.IntegerField', [], {'default': '1500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'site_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'frontend.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "u'tags'"},
            'always_fill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'floor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'frequency_cap': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_daily_impressions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Network']"}),
            'pacing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Publisher']"}),
            'rejection_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sample_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'frontend.tagoption': {
            'Meta': {'object_name': 'TagOption', 'db_table': "u'tag_options'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'option_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Tag']"})
        },
        'frontend.tagtarget': {
            'Meta': {'object_name': 'TagTarget', 'db_table': "u'tag_targets'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'key_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['frontend.Tag']"})
        }
    }

    complete_apps = ['frontend']
