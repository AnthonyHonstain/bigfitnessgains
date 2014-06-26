from django.contrib.auth import get_user_model
import django_measurement.utils

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
    '''
    WARNING - non-obvious logic in place to deal with serializing
    the Weight measurement field on the WorkoutSet model.
    '''

    # Sourcing the 'user_weight_value' from a helper method
    # on the WorkoutSet model.
    user_weight_value = serializers.FloatField(source='weight_value')
    # NOTICE - there is a field for user_weight_value AND weight_value,
    # BUT we only want users supplying a user_weight_value.
    weight_value = serializers.FloatField(required=False)
    weight_unit = serializers.CharField()
    weight_measure = serializers.CharField(default='Weight(g)')

    def to_native(self, obj):
        ret = super(serializers.ModelSerializer, self).to_native(obj)

        # Using the weight unit from the WorkoutSet
        unit = obj.weight_unit
        # Assuming the value is in grams
        weight = Weight(g=obj.weight_value)
        ret['user_weight_value'] = getattr(weight, unit)
        return ret

    def from_native(self, data, files):
        standard_weight_unit = Weight.STANDARD_UNIT
        # Construct a Weight instance from the user data.
        converted_value = django_measurement.utils.get_measurement(Weight,
                                                                   data['user_weight_value'],
                                                                   data['weight_unit'])
        # We want the weight_value in grams
        data['weight_value'] = getattr(converted_value, standard_weight_unit)
        ret = super(serializers.ModelSerializer, self).from_native(data, files)
        return ret

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

        read_only_fields = ('created',
                            'modified')


class WorkoutSetGetSerializer(WorkoutSetBaseSerializer):

    workout_fk = WorkoutSerializer()
    exercise_fk = ExerciseBaseSerializer()


class WorkoutSetPutSerializer(WorkoutSetBaseSerializer):
    '''
    WorkoutSet serializer for PUT functionality, we don't ALLOW
    modification of the workout_fk after a WorkoutSet has been created.
    '''

    class Meta:
        model = WorkoutSet
        fields = ('id',
                  #'workout_fk',
                  'exercise_fk',
                  'reps',
                  'weight_value',
                  'weight_unit',
                  'weight_measure',
                  'order')

        read_only_fields = ('workout_fk',
                            'created',
                            'modified')


## http://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
