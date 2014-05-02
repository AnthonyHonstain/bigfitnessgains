# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table(u'mainapp_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('muscle_groups_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.ExerciseToMuscleGroup'])),
        ))
        db.send_create_signal(u'mainapp', ['Exercise'])

        # Adding model 'ExerciseToMuscleGroup'
        db.create_table(u'mainapp_exercisetomusclegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Exercise'])),
            ('muscle_group_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.MuscleGroup'])),
        ))
        db.send_create_signal(u'mainapp', ['ExerciseToMuscleGroup'])

        # Adding model 'MuscleGroup'
        db.create_table(u'mainapp_musclegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('muscle_group_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mainapp', ['MuscleGroup'])

        # Adding model 'Workout'
        db.create_table(u'mainapp_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.UserProfile'])),
            ('workout_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mainapp', ['Workout'])

        # Adding model 'WorkoutSet'
        db.create_table(u'mainapp_workoutset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.UserProfile'])),
            ('workout_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Workout'])),
            ('exercise_fk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Exercise'])),
            ('reps', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'mainapp', ['WorkoutSet'])

        # Adding model 'UserProfile'
        db.create_table(u'mainapp_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mainapp', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table(u'mainapp_exercise')

        # Deleting model 'ExerciseToMuscleGroup'
        db.delete_table(u'mainapp_exercisetomusclegroup')

        # Deleting model 'MuscleGroup'
        db.delete_table(u'mainapp_musclegroup')

        # Deleting model 'Workout'
        db.delete_table(u'mainapp_workout')

        # Deleting model 'WorkoutSet'
        db.delete_table(u'mainapp_workoutset')

        # Deleting model 'UserProfile'
        db.delete_table(u'mainapp_userprofile')


    models = {
        u'mainapp.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'exercise_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle_groups_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.ExerciseToMuscleGroup']"})
        },
        u'mainapp.exercisetomusclegroup': {
            'Meta': {'object_name': 'ExerciseToMuscleGroup'},
            'exercise_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle_group_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.MuscleGroup']"})
        },
        u'mainapp.musclegroup': {
            'Meta': {'object_name': 'MuscleGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscle_group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.workout': {
            'Meta': {'object_name': 'Workout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.UserProfile']"}),
            'workout_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.workoutset': {
            'Meta': {'object_name': 'WorkoutSet'},
            'exercise_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.UserProfile']"}),
            'reps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'workout_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Workout']"})
        }
    }

    complete_apps = ['mainapp']