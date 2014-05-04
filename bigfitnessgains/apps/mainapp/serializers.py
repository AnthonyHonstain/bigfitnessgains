from bigfitnessgains.apps.mainapp.models import Exercise, ExerciseToMuscleGroup, MuscleGroup, Workout, WorkoutSet
from rest_framework import serializers

class ExerciseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Exercise
		fields = ('id', 'exercise_name', 'muscle_groups_fk')	

class ExerciseToMuscleGroupSerializer(serializers.ModelSerializer):
	""" We may not need this """

	class Meta:
		model = ExerciseToMuscleGroup
		fields = ('id', 'exercise_fk', 'muscle_group_fk')

class MuscleGroupSerializer(serializers.ModelSerializer):
	""" Also may not be needed in the REST API """

	class Meta:
		model = MuscleGroup
		fields = ('id', 'muscle_group_name')

class WorkoutSerializer(serializers.ModelSerializer):

	class Meta:
		model = Workout
		fields = ('id', 'user_fk', 'workout_name')

class WorkoutSetSerializer(serializers.ModelSerializer):

	class Meta:
		model = WorkoutSet
		fields = ('id', 'user_fk', 'workout_fk', 'exercise_fk', 'reps', 'weight')