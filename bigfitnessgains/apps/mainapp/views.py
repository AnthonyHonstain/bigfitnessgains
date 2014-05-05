from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bigfitnessgains.apps.mainapp import utils
from bigfitnessgains.apps.mainapp.models import Exercise, ExerciseToMuscleGroup, MuscleGroup, Workout, WorkoutSet
from bigfitnessgains.apps.mainapp.serializers import ExerciseSerializer, ExerciseToMuscleGroupSerializer, MuscleGroupSerializer, WorkoutSerializer, WorkoutSetSerializer


def index(request):
    return render(request, 'mainapp/index.html', None)

@csrf_exempt
def exercise_list(request):
	if request.method == 'GET':
		exercises = Exercise.objects.all()
		serializer = ExerciseSerializer(exercises, many=True)
		return utils.JSONResponse(serializer.data)

	if request.method == 'POST':
		pass

@csrf_exempt
def workout_list(request):
	if request.method == 'GET':
		workouts = Workout.objects.all()
		serializer = WorkoutSerializer(workouts, many=True)
		return utils.JSONResponse(serializer.data)

	if request.method == 'POST':
		pass

@csrf_exempt
def set_list(request):
	if request.method == 'GET':
		sets = WorkoutSet.objects.all()
		serializer = WorkoutSetSerializer(sets, many=True)
		return utils.JSONResponse(serializer.data)

	if request.method == 'POST':
		pass

@csrf_exempt
def muscle_group_list(request):
	if request.method == 'GET':
		groups = MuscleGroup.objects.all()
		serializer = MuscleGroupSerializer(groups, many=True)
		return utils.JSONResponse(serializer.data)

	if request.method == 'POST':
		pass
		