from bigfitnessgains.apps.mainapp.models import Exercise
from bigfitnessgains.apps.mainapp.serializers import ExerciseSerializer

from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     )


class ExerciseList(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(RetrieveAPIView):
    '''
    By extending RetrieveAPIView we are Just going to expose
    the retrieve functionality, not update/delete (we need
    to figure out permissions scenario around that first).
    '''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
