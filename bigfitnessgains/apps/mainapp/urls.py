from django.conf.urls import patterns, url
from bigfitnessgains.apps.mainapp.rest_api.exercise import ExerciseList, ExerciseDetail
from bigfitnessgains.apps.mainapp.rest_api.workout import WorkoutListAPI, WorkoutDetailAPI
from bigfitnessgains.apps.mainapp.rest_api.workoutset import (WorkoutSetListAPI,
                                                              WorkoutSetDetailAPI,
                                                              WorkoutSetOrder,
                                                              )

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^workout/$', views.workout, name='workout'),
    url(r'^workout_detail/(?P<pk>[0-9]+)/$', views.workout_detail, name='workout_detail'),

    url(r'^exercise/$', ExerciseList.as_view(), name='exercise_list'),
    url(r'^exercise/(?P<pk>[0-9]+)/$', ExerciseDetail.as_view(), name='exercise_detail'),

    url(r'^workouts/$', WorkoutListAPI.as_view()),
    url(r'^workouts/(?P<pk>[0-9]+)/$', WorkoutDetailAPI.as_view()),

    url(r'^workout_sets/$', WorkoutSetListAPI.as_view()),
    url(r'^workout_sets/(?P<pk>[0-9]+)/$', WorkoutSetDetailAPI.as_view()),

	# This should probably move to workouts/ since the pk is for a workout
	# and not a workout_set (we only care about workout_set records in the context
    # of the workout they are associated with.
    url(r'^workout_sets/(?P<pk>[0-9]+)/order/$', WorkoutSetOrder.as_view(), name='workoutset_order'),

    #url(r'^exercises/$', views.exercise_list, name='exercises'),
    #url(r'^muscle_groups/$', views.muscle_group_list, name='muscle_groups')
)
