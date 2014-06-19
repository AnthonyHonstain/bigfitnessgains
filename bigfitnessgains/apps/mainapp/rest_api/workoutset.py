from bigfitnessgains.apps.mainapp.models import Workout
from bigfitnessgains.apps.mainapp.models import WorkoutSet
from bigfitnessgains.apps.mainapp.serializers import (WorkoutSetBaseSerializer,
                                                      WorkoutSetGetSerializer,
                                                      )
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WorkoutSetListAPI(APIView):
    ''' Defines an APIView class to use for WorkoutSet object REST requests.
        See notes on WorkoutSetBaseSerializer vs WorkoutSetGetSerializer in serializers.py
    '''
    def get(self, request, format=None):
        sets = WorkoutSet.objects.all()
        serializer = WorkoutSetGetSerializer(sets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutSetBaseSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutSetDetailAPI(APIView):
    ''' Defines an APIView class to use for WorkoutSet object REST requests by id (single record).
        See notes on WorkoutSetBaseSerializer vs WorkoutSetGetSerializer in serializers.py
    '''
    def _get_object(self, pk):
        try:
            return WorkoutSet.objects.get(pk=pk)
        except WorkoutSet.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        w_set = self._get_object(pk)
        serializer = WorkoutSetBaseSerializer(w_set)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        w_set = self._get_object(pk)
        serializer = WorkoutSetBaseSerializer(w_set, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        w_set = self._get_object(pk)
        w_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkoutSetBase(APIView):

    def _check_workout_permissions(self, workout_fk):
        '''
        Splitting this out for extra clarity
        '''
        # Get the Workout object requested, if it exists
        obj = get_object_or_404(Workout, pk=workout_fk)
        # Check permissions on it (workoutset doesn't track user).

        if obj.user_fk != self.request.user:
            self.permission_denied(self.request)

    def _get_workoutset(self, workout_fk):
        self._check_workout_permissions(workout_fk)

        workoutset = WorkoutSet.objects.filter(workout_fk=workout_fk).select_related('workout_fk', 'exercise_fk')
        # TODO - can I clean up the permission checks?
        #print 'foo', workoutset
        return workoutset


class WorkoutSetOrder(WorkoutSetBase):
    '''
    Special API to support drag and drop re-order of the workoutset items by the client.
    '''

    def get(self, request, workout_fk, format=None):
        sets = self._get_workoutset(workout_fk)
        serializer = WorkoutSetGetSerializer(sets, many=True)
        return Response(serializer.data)

    def post(self, request, workout_fk, format=None):
        serializer = WorkoutSetBaseSerializer(data=request.DATA)
        if serializer.is_valid():
            self._check_workout_permissions(workout_fk)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutSetOrderUpdate(WorkoutSetBase):

#     def _get_object(self, pk):
#         try:
#             return WorkoutSet.objects.get(pk=pk)
#         except WorkoutSet.DoesNotExist:
#             return Http404

    def get(self, request, workout_fk, pk, format=None):
        workoutset = WorkoutSet.objects.select_related('workout_fk', 'exercise_fk').get(pk=pk)
        if workoutset.workout_fk.user_fk != self.request.user:
            self.permission_denied(self.request)

        serializer = WorkoutSetGetSerializer(workoutset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workoutset = WorkoutSet.objects.select_related('workout_fk').get(pk=pk)
        if workoutset.workout_fk.user_fk != self.request.user:
            self.permission_denied(self.request)

        serializer = WorkoutSetBaseSerializer(workoutset, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workoutset = WorkoutSet.objects.select_related('workout_fk').get(pk=pk)
        if workoutset.workout_fk.user_fk != self.request.user:
            self.permission_denied(self.request)

        workoutset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

