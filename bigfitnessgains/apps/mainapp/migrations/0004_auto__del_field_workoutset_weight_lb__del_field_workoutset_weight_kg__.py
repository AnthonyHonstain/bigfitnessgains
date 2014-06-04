# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'WorkoutSet.weight_lb'
        db.delete_column(u'mainapp_workoutset', 'weight_lb')

        # Deleting field 'WorkoutSet.weight_kg'
        db.delete_column(u'mainapp_workoutset', 'weight_kg')

        # Adding field 'WorkoutSet.weight_unit'
        db.add_column(u'mainapp_workoutset', 'weight_unit',
                      self.gf('django_measurement.fields.OriginalUnitField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'WorkoutSet.weight_measure'
        db.add_column(u'mainapp_workoutset', 'weight_measure',
                      self.gf('django_measurement.fields.MeasureNameField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'WorkoutSet.weight_value'
        db.add_column(u'mainapp_workoutset', 'weight_value',
                      self.gf('django_measurement.fields.MeasurementValueField')(default=0.0, max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'WorkoutSet.weight_lb'
        db.add_column(u'mainapp_workoutset', 'weight_lb',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'WorkoutSet.weight_kg'
        db.add_column(u'mainapp_workoutset', 'weight_kg',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Deleting field 'WorkoutSet.weight_unit'
        db.delete_column(u'mainapp_workoutset', 'weight_unit')

        # Deleting field 'WorkoutSet.weight_measure'
        db.delete_column(u'mainapp_workoutset', 'weight_measure')

        # Deleting field 'WorkoutSet.weight_value'
        db.delete_column(u'mainapp_workoutset', 'weight_value')


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
            'muscle_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MuscleGroup']", 'through': u"orm['mainapp.ExerciseToMuscleGroup']", 'symmetrical': 'False'})
        },
        u'mainapp.exercisetomusclegroup': {
            'Meta': {'object_name': 'ExerciseToMuscleGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'exercise_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'muscle_group_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.MuscleGroup']"})
        },
        u'mainapp.musclegroup': {
            'Meta': {'object_name': 'MuscleGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Exercise']", 'through': u"orm['mainapp.ExerciseToMuscleGroup']", 'symmetrical': 'False'}),
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
            'reps': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'weight_measure': ('django_measurement.fields.MeasureNameField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'weight_unit': ('django_measurement.fields.OriginalUnitField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'weight_value': ('django_measurement.fields.MeasurementValueField', [], {'default': '0.0', 'max_length': '50', 'blank': 'True'}),
            'workout_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Workout']"})
        }
    }

    complete_apps = ['mainapp']