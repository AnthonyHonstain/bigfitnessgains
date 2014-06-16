from django.contrib import admin

import models

admin.site.register(models.MuscleGroup)
admin.site.register(models.Exercise)

admin.site.register(models.Workout)


class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = ('workout_fk', 'exercise_fk', 'reps', 'weight', 'order',)
    list_filter = ('workout_fk__user_fk',)

admin.site.register(models.WorkoutSet, WorkoutSetAdmin)
