from django.contrib import admin
from django_measurement.admin import MeasurementAdmin

import models

admin.site.register(models.MuscleGroup)
admin.site.register(models.Exercise)

admin.site.register(models.Workout)


class WorkoutSetAdmin(MeasurementAdmin):
    list_display = ('workout_fk', 'exercise_fk', 'reps', 'weight', 'order',)
    # TODO - need to be smarter about filtering as number of different workouts grow.
    list_filter = ('workout_fk__user_fk', 'workout_fk')

admin.site.register(models.WorkoutSet, WorkoutSetAdmin)
