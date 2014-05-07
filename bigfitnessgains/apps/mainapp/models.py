from django.db import models
from django.contrib.auth.models import User

## save() auto-date method reference: 
## http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078

class TrackCreatedUpdatedModel(models.Model):
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    class Meta:
        abstract        = True

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(TrackCreatedUpdatedModel, self).save(*args, **kwargs)

class Exercise(TrackCreatedUpdatedModel):
    exercise_name       = models.CharField(max_length=100, unique=True)
    muscle_groups_fk    = models.ForeignKey('ExerciseToMuscleGroup')
    

class ExerciseToMuscleGroup(TrackCreatedUpdatedModel):
    exercise_fk         = models.ForeignKey('Exercise')
    muscle_group_fk     = models.ForeignKey('MuscleGroup')


class MuscleGroup(TrackCreatedUpdatedModel):
    muscle_group_name   = models.CharField(max_length=100, unique=True)
    

class Workout(TrackCreatedUpdatedModel):
    user_fk             = models.ForeignKey(User)
    workout_name        = models.CharField(max_length=100)
    workout_date        = models.DateTimeField()


class WorkoutSet(TrackCreatedUpdatedModel):
    workout_fk          = models.ForeignKey('Workout')
    exercise_fk         = models.ForeignKey('Exercise')
    reps                = models.PositiveIntegerField()
    weight_lb           = models.DecimalField(max_digits=10, decimal_places=2)
    weight_kg           = models.DecimalField(max_digits=10, decimal_places=2)