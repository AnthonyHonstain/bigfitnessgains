# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ExerciseToMuscleGroup'
        db.delete_table(u'mainapp_exercisetomusclegroup')

        # Deleting field 'Exercise.muscle_groups_fk'
        db.delete_column(u'mainapp_exercise', 'muscle_groups_fk_id')

        # Adding field 'Exercise.muscle_group_fk'
        db.add_column(u'mainapp_exercise', 'muscle_group_fk',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mainapp.MuscleGroup']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ExerciseToMuscleGroup'
        db.create_table(u'mainapp_exercisetomusclegroup', (
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('exercise_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Exercise'])),
            ('muscle_group_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.MuscleGroup'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mainapp', ['ExerciseToMuscleGroup'])

        # Adding field 'Exercise.muscle_groups_fk'
        db.add_column(u'mainapp_exercise', 'muscle_groups_fk',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['mainapp.ExerciseToMuscleGroup']),
                      keep_default=False)

        # Deleting field 'Exercise.muscle_group_fk'
        db.delete_column(u'mainapp_exercise', 'muscle_group_fk_id')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'exercise_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'muscle_group_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.MuscleGroup']"})
        },
        u'mainapp.musclegroup': {
            'Meta': {'object_name': 'MuscleGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'muscle_group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'mainapp.workout': {
            'Meta': {'object_name': 'Workout'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'user_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'workout_date': ('django.db.models.fields.DateTimeField', [], {}),
            'workout_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.workoutset': {
            'Meta': {'object_name': 'WorkoutSet'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'exercise_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'reps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'weight_kg': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'weight_lb': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'workout_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Workout']"})
        }
    }

    complete_apps = ['mainapp']