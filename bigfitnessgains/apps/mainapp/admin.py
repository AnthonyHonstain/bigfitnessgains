from django.contrib import admin

import models

admin.site.register(models.MuscleGroup)
admin.site.register(models.Exercise)

admin.site.register(models.Workout)
admin.site.register(models.WorkoutSet)
