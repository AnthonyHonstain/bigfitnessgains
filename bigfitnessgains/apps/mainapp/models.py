import datetime

from django.db import models
from django.contrib.auth.models import User

## save() auto-date method reference:
## http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078


class TrackCreatedUpdatedModel(models.Model):
    '''
    Note we have implemented our own instead of using the auto create/modified
    functionality provided by django.
        http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    '''
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


class ExerciseToMuscleGroup(TrackCreatedUpdatedModel):
    exercise_fk         = models.ForeignKey('Exercise')
    muscle_group_fk     = models.ForeignKey('MuscleGroup')
    is_primary          = models.BooleanField()


class Exercise(TrackCreatedUpdatedModel):
    exercise_name       = models.CharField(max_length=100, unique=True)
    muscle_groups       = models.ManyToManyField('MuscleGroup', through=ExerciseToMuscleGroup)

    def __str__(self):
        return self.exercise_name


class MuscleGroup(TrackCreatedUpdatedModel):
    muscle_group_name   = models.CharField(max_length=100, unique=True)
    exercises           = models.ManyToManyField('Exercise', through=ExerciseToMuscleGroup)

    def __str__(self):
        return self.muscle_group_name


class Workout(TrackCreatedUpdatedModel):
    user_fk             = models.ForeignKey(User)
    workout_name        = models.CharField(max_length=100)
    workout_date        = models.DateTimeField()

    def __str__(self):
        return self.workout_name


class WorkoutSet(TrackCreatedUpdatedModel):
    workout_fk          = models.ForeignKey('Workout')
    exercise_fk         = models.ForeignKey('Exercise')
    reps                = models.PositiveIntegerField(default=1)
    weight_lb           = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight_kg           = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        # TODO - notice extra query here
        return '{0} - {1}'.format(self.workout_fk.workout_name, self.exercise_fk)
