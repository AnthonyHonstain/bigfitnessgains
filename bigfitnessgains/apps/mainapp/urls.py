from django.conf.urls import patterns, url
 
import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^exercises/$', views.exercise_list, name='exercises'),
    url(r'^workouts/$', views.workout_list, name='workouts'),
    url(r'^workout_sets/$', views.set_list, name='workout_sets'),
    url(r'^muscle_groups/$', views.muscle_group_list, name='muscle_groups')
)
