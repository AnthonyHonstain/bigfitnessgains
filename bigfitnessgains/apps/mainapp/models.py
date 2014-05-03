from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
	exercise_name = models.CharField(max_length=100)
	muscle_groups_fk = models.ForeignKey('ExerciseToMuscleGroup')


class ExerciseToMuscleGroup(models.Model):
	exercise_fk = models.ForeignKey('Exercise')
	muscle_group_fk = models.ForeignKey('MuscleGroup')


class MuscleGroup(models.Model):
	muscle_group_name = models.CharField(max_length=100)


class Workout(models.Model):
	user_fk = models.ForeignKey(User)
	workout_name = models.CharField(max_length=100)


class WorkoutSet(models.Model):
	profile_fk = models.ForeignKey(User)
	workout_fk = models.ForeignKey('Workout')
	exercise_fk = models.ForeignKey('Exercise')
	reps = models.PositiveIntegerField()
	weight = models.DecimalField(max_digits=10, decimal_places=2)

