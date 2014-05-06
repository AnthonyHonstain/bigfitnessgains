from django.conf.urls import patterns, url
from bigfitnessgains.apps.mainapp.rest_api.workout import WorkoutListAPI, WorkoutDetailAPI
from bigfitnessgains.apps.mainapp.rest_api.workoutset import WorkoutSetListAPI, WorkoutSetDetailAPI
 
import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^workouts/$', WorkoutListAPI.as_view()),
    url(r'^workouts/(?P<pk>[0-9]+)/$', WorkoutDetailAPI.as_view()),

    url(r'^workout_sets/$', WorkoutSetListAPI.as_view()),
    url(r'^workout_sets/(?P<pk>[0-9]+)/$', WorkoutSetDetailAPI.as_view()),

    #url(r'^exercises/$', views.exercise_list, name='exercises'),
    #url(r'^muscle_groups/$', views.muscle_group_list, name='muscle_groups')
)
