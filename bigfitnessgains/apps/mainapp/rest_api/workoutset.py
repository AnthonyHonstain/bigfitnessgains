from bigfitnessgains.apps.mainapp.models import Workout
from bigfitnessgains.apps.mainapp.models import WorkoutSet
from bigfitnessgains.apps.mainapp.serializers import (WorkoutSetBaseSerializer,
                                                      WorkoutSetGetSerializer,
                                                      WorkoutSetOrderSerializer,
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


from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     )


class WorkoutSetOrder(ListAPIView):
    '''
    Special API to support drag and drop re-order of the workoutset items by the client.
    '''

    serializer_class = WorkoutSetOrderSerializer

    def get_queryset(self):

        workout_fk = self.kwargs[self.lookup_field]

        obj = get_object_or_404(Workout, pk=workout_fk)
        self.check_object_permissions(self.request, obj)
        queryset = WorkoutSet.objects.filter(workout_fk=obj)
        # TODO - will I want to break this filtering logic out to a mixin
        # that I can share? http://www.django-rest-framework.org/api-guide/generic-views
        return queryset


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
