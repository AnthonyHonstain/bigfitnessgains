from bigfitnessgains.apps.mainapp.models import Workout
from bigfitnessgains.apps.mainapp.models import WorkoutSet
from bigfitnessgains.apps.mainapp.serializers import (WorkoutSetBaseSerializer,
                                                      WorkoutSetGetSerializer,
                                                      WorkoutSetPutSerializer,
                                                      )
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

'''
TODO - for the future we should consider transitioning these to take advantage
of the django REST framework permissions support.
'''


class WorkoutSetList(APIView):
    '''
    GET and POST using a Workout.

    GET - List all the WorkoutSet records for a Workout.
        Result includes serialized Workout and Exercise foreign key relationships
    POST - Create a new WorkoutSet for a Workout.
        Input - has special logic for weight.
        Result includes serialized Workout and Exercise foreign key relationships

    See notes on WorkoutSetBaseSerializer vs WorkoutSetGetSerializer in serializers.py
    '''

    def get(self, request, workout_fk, format=None):
        '''
        Retrieve all the WorkoutSet records for a given Workout.
        '''
        self._check_workout_permissions(workout_fk)

        workoutset_queryset = WorkoutSet.objects.filter(workout_fk=workout_fk)\
            .select_related('workout_fk', 'exercise_fk')

        serializer = WorkoutSetGetSerializer(workoutset_queryset, many=True)
        return Response(serializer.data)

    def post(self, request, workout_fk, format=None):
        '''
        Create a new WorkoutSet for a given Workout.
        '''
        serializer = WorkoutSetBaseSerializer(data=request.DATA)

        if serializer.is_valid():
            self._check_workout_permissions(workout_fk)
            serializer.save()

            # WARNING - We want to return the WorkoutSet WITH Workout and Exercise
            # info, it might be possible to rodeo this into the serializer.
            workoutset = WorkoutSet.objects.select_related('workout_fk', 'exercise_fk').get(pk=serializer.data['id'])
            extended_serializer = WorkoutSetGetSerializer(workoutset)

            return Response(extended_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _check_workout_permissions(self, workout_fk):
        '''
        Verify the request user owns this workout
        '''
        workout_obj = get_object_or_404(Workout, pk=workout_fk)

        # Check permissions on it (workoutset doesn't track user).
        if workout_obj.user_fk != self.request.user:
            self.permission_denied(self.request)


class WorkoutSetDetail(APIView):
    '''
    GET, PUT, DELETE using a WorkoutSet id.

    See notes on WorkoutSetBaseSerializer vs WorkoutSetGetSerializer in serializers.py
    '''

    def get(self, request, workout_fk, pk, format=None):
        '''
        Retrieve a single workoutset.
        '''
        workoutset = WorkoutSet.objects.select_related('workout_fk', 'exercise_fk').get(pk=pk)
        self._check_workoutset_permissions(workout_fk, workoutset)

        serializer = WorkoutSetGetSerializer(workoutset)
        return Response(serializer.data)

    def put(self, request, workout_fk, pk, format=None):
        '''
        Update a single workoutset.
        '''
        workoutset = WorkoutSet.objects.select_related('workout_fk').get(pk=pk)
        self._check_workoutset_permissions(workout_fk, workoutset)

        # We have a special PUT serializer, to prevent the user from
        # changing the workout_fk
        serializer = WorkoutSetPutSerializer(workoutset, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, workout_fk, pk, format=None):
        '''
        Delete a single workoutset.
        '''
        workoutset = WorkoutSet.objects.select_related('workout_fk').get(pk=pk)
        self._check_workoutset_permissions(workout_fk, workoutset)

        workoutset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _check_workoutset_permissions(self, workout_fk, workoutset):
        '''
        A basic check which assumes the workoutset was queryed with
        select related for workout_fk (so we also have the workout record.
        '''
        # Make sure the request user owns the workout
        if (workoutset.workout_fk.user_fk != self.request.user):
            self.permission_denied(self.request)

        # Make sure the workout_fk matches what was provided in the data.
        if workoutset.workout_fk.id != int(workout_fk):
            self.permission_denied(self.request)
