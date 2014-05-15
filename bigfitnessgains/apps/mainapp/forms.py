
from django import forms
from models import Workout
from models import WorkoutSet


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        exclude = ['user_fk', 'modified']


class WorkoutSetForm(forms.ModelForm):

    class Meta:
        model = WorkoutSet
        exclude = ['workout_fk', 'modified']
