# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'userui_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_Of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('Notes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
        ))
        db.send_create_signal(u'userui', ['UserProfile'])

        # Adding model 'UserBlocks'
        db.create_table(u'userui_userblocks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userui.UserProfile'])),
        ))
        db.send_create_signal(u'userui', ['UserBlocks'])

        # Adding unique constraint on 'UserBlocks', fields ['user', 'number']
        db.create_unique(u'userui_userblocks', ['user_id', 'number'])

        # Adding model 'Trial'
        db.create_table(u'userui_trial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trialNumber', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('task_text', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('pointA', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pointB', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('expectedAnswer', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('blockId', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('technique', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('task', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'userui', ['Trial'])

        # Adding unique constraint on 'Trial', fields ['trialNumber', 'blockId', 'order']
        db.create_unique(u'userui_trial', ['trialNumber', 'blockId', 'order'])

        # Adding model 'Results'
        db.create_table(u'userui_results', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userui.UserProfile'])),
            ('blockID', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('trialID', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('userAnswer', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('time', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=3)),
        ))
        db.send_create_signal(u'userui', ['Results'])

        # Adding unique constraint on 'Results', fields ['uID', 'blockID', 'trialID']
        db.create_unique(u'userui_results', ['uID_id', 'blockID', 'trialID'])

        # Adding model 'Colortest'
        db.create_table(u'userui_colortest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userui.UserProfile'])),
            ('answer_1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer_2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer_3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer_4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer_5', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer_6', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'userui', ['Colortest'])


    def backwards(self, orm):
        # Removing unique constraint on 'Results', fields ['uID', 'blockID', 'trialID']
        db.delete_unique(u'userui_results', ['uID_id', 'blockID', 'trialID'])

        # Removing unique constraint on 'Trial', fields ['trialNumber', 'blockId', 'order']
        db.delete_unique(u'userui_trial', ['trialNumber', 'blockId', 'order'])

        # Removing unique constraint on 'UserBlocks', fields ['user', 'number']
        db.delete_unique(u'userui_userblocks', ['user_id', 'number'])

        # Deleting model 'UserProfile'
        db.delete_table(u'userui_userprofile')

        # Deleting model 'UserBlocks'
        db.delete_table(u'userui_userblocks')

        # Deleting model 'Trial'
        db.delete_table(u'userui_trial')

        # Deleting model 'Results'
        db.delete_table(u'userui_results')

        # Deleting model 'Colortest'
        db.delete_table(u'userui_colortest')


    models = {
        u'userui.colortest': {
            'Meta': {'object_name': 'Colortest'},
            'answer_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answer_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answer_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answer_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answer_5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answer_6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userui.UserProfile']"})
        },
        u'userui.results': {
            'Meta': {'unique_together': "(('uID', 'blockID', 'trialID'),)", 'object_name': 'Results'},
            'blockID': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '3'}),
            'trialID': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userui.UserProfile']"}),
            'userAnswer': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'userui.trial': {
            'Meta': {'unique_together': "(('trialNumber', 'blockId', 'order'),)", 'object_name': 'Trial'},
            'blockId': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'expectedAnswer': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pointA': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pointB': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task_text': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'technique': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trialNumber': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'userui.userblocks': {
            'Meta': {'unique_together': "(('user', 'number'),)", 'object_name': 'UserBlocks'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userui.UserProfile']"})
        },
        u'userui.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'Notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_Of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        }
    }

    complete_apps = ['userui']