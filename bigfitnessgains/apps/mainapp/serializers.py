from django.contrib.auth import get_user_model

from bigfitnessgains.apps.mainapp.models import Exercise, MuscleGroup, Workout, WorkoutSet
from rest_framework import serializers
from measurement.measures.weight import Weight

## http://www.django-rest-framework.org/api-guide/serializers
## TODO: add transforms and validations where appropriate


class MuscleGroupSerializer(serializers.ModelSerializer):
    """ Also may not be needed in the REST API """

    # TODO: figure out how to expose is_primary through the API for each muscle group in an exercise

    class Meta:
        model = MuscleGroup
        fields = ('id', 'muscle_group_name')
        read_only_fields = ('created', 'modified')


class ExerciseBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        # Removing modified field, REST api expects modified field as input
        #(which is  a problem because we expect the model to set it).
        fields = ('id', 'exercise_name', 'muscle_groups')
        read_only_fields = ('created', 'modified')


class ExerciseSerializer(ExerciseBaseSerializer):

    muscle_groups = MuscleGroupSerializer(many=True)


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'user_fk', 'workout_name', 'workout_date')
        read_only_fields = ('created', 'modified')


class WorkoutSetBaseSerializer(serializers.ModelSerializer):

    def transform_weight_value(self, obj, value):
        ''' Override and convert the weight_value into whatever weight_unit it was stored as.
            Unfortunately we don't have a user context to use preferences, but at least this makes
            the tuple (weight_value, weight_unit) make sense
        '''
        if value: # chance this comes back to bite me: 140%
            unit = obj.weight_unit
            weight = Weight(g=value)
            return getattr(weight, unit)
        return None

    class Meta:
        model = WorkoutSet
        fields = ('id',
                  'workout_fk',
                  'exercise_fk',
                  'reps',
                  'weight_value',
                  'weight_unit',
                  'weight_measure',
                  'order')
        read_only_fields = ('created', 'modified')


class WorkoutSetGetSerializer(WorkoutSetBaseSerializer):

    workout_fk = WorkoutSerializer()
    exercise_fk = ExerciseBaseSerializer()

## http://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
