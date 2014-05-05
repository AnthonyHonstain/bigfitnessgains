from django.db import models
from django.contrib.auth.models import User

## save() auto-date method reference: 
## http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078

class Exercise(models.Model):
    exercise_name       = models.CharField(max_length=100, unique=True)
    muscle_groups_fk    = models.ForeignKey('ExerciseToMuscleGroup')
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Exercise, self).save(*args, **kwargs)

class ExerciseToMuscleGroup(models.Model):
    exercise_fk         = models.ForeignKey('Exercise')
    muscle_group_fk     = models.ForeignKey('MuscleGroup')
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(ExerciseToMuscleGroup, self).save(*args, **kwargs)

class MuscleGroup(models.Model):
    muscle_group_name   = models.CharField(max_length=100, unique=True)
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(MuscleGroup, self).save(*args, **kwargs)

class Workout(models.Model):
    user_fk             = models.ForeignKey(User)
    workout_name        = models.CharField(max_length=100)
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Workout, self).save(*args, **kwargs)

class WorkoutSet(models.Model):
    profile_fk          = models.ForeignKey(User)
    workout_fk          = models.ForeignKey('Workout')
    exercise_fk         = models.ForeignKey('Exercise')
    reps                = models.PositiveIntegerField()
    weight              = models.DecimalField(max_digits=10, decimal_places=2)
    created             = models.DateTimeField(editable=False)
    modified            = models.DateTimeField()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(WorkoutSet, self).save(*args, **kwargs)