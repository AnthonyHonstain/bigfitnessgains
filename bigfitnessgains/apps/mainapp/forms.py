
from django import forms
from models import Workout
from models import WorkoutSet
from django_measurement.forms import MeasurementFormMixin, MeasurementFormField
from measurement.measures import Weight


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        exclude = ['user_fk', 'modified']


class WorkoutSetForm(MeasurementFormMixin, forms.ModelForm):

    weight = MeasurementFormField(measurement=Weight, choices=(('kg', 'kg'), ('lb', 'lb')))

    class Meta:
        model = WorkoutSet
        exclude = ['workout_fk', 'modified']
