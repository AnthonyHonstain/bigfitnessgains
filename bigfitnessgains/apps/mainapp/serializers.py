from django.contrib.auth import get_user_model

from bigfitnessgains.apps.mainapp.models import Exercise, MuscleGroup, Workout, WorkoutSet
from rest_framework import serializers

## http://www.django-rest-framework.org/api-guide/serializers
## TODO: add transforms and validations where appropriate


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        # Removing modified field, REST api expects modified field as input
        #(which is  a problem because we expect the model to set it).
        fields = ('id', 'exercise_name', 'muscle_group_fk') #, 'created', 'modified')


# class ExerciseToMuscleGroupSerializer(serializers.ModelSerializer):
#     """ We may not need this """
#
#     class Meta:
#         model = ExerciseToMuscleGroup
#         fields = ('id', 'exercise_fk', 'muscle_group_fk', 'created', 'modified')


class MuscleGroupSerializer(serializers.ModelSerializer):
    """ Also may not be needed in the REST API """

    class Meta:
        model = MuscleGroup
        fields = ('id', 'muscle_group_name', 'created', 'modified')


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'user_fk', 'workout_name', 'workout_date', 'created', 'modified')


class WorkoutSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutSet
        fields = ('id', 'workout_fk', 'exercise_fk', 'reps', 'weight_lb', 'weight_kg', 'created', 'modified')


## http://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
