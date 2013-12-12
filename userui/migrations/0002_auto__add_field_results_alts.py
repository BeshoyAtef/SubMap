# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Results.alts'
        db.add_column(u'userui_results', 'alts',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Results.alts'
        db.delete_column(u'userui_results', 'alts')


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
            'alts': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
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