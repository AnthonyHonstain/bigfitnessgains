from bigfitnessgains.apps.mainapp.models import WorkoutSet
from bigfitnessgains.apps.mainapp.serializers import WorkoutSetBaseSerializer, WorkoutSetGetSerializer
from django.http import Http404
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
