from django.conf.urls import patterns, url
from bigfitnessgains.apps.mainapp.rest_api.exercise import ExerciseList, ExerciseDetail
from bigfitnessgains.apps.mainapp.rest_api.workout import WorkoutListAPI, WorkoutDetailAPI
from bigfitnessgains.apps.mainapp.rest_api.workoutset import (WorkoutSetListAPI,
                                                              WorkoutSetDetailAPI,
                                                              WorkoutSetOrder,
                                                              WorkoutSetOrderUpdate,
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

    # Crafting some special REST endpoint for working with the workoutsets
    # via AJAX.
    url(r'^workouts/(?P<workout_fk>[0-9]+)/workoutsets/$',
        WorkoutSetOrder.as_view(),
        name='workoutset_list'),
    url(r'^workouts/(?P<workout_fk>[0-9]+)/workoutsets/(?P<pk>[0-9]+)/$',
        WorkoutSetOrderUpdate.as_view(),
        name='workoutset_detail'),

    url(r'^workout_sets/$', WorkoutSetListAPI.as_view()),
    url(r'^workout_sets/(?P<pk>[0-9]+)/$', WorkoutSetDetailAPI.as_view()),

    #url(r'^exercises/$', views.exercise_list, name='exercises'),
    #url(r'^muscle_groups/$', views.muscle_group_list, name='muscle_groups')
)
