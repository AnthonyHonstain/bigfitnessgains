from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.db import transaction

from bigfitnessgains.apps.mainapp.forms import WorkoutForm
from bigfitnessgains.apps.mainapp.forms import WorkoutSetForm
from bigfitnessgains.apps.mainapp.models import Workout
from bigfitnessgains.apps.mainapp.models import WorkoutSet


def index(request):
    return render(request, 'mainapp/index.html', None)


'''
********************************************************************
WARNING - prototype
    This may be better modeled with a class based view, the models
    are also expected to be heavily massaged.

    TODO - still need to game plan the dashboard.
********************************************************************
'''
@login_required(login_url='/accounts/signin/')
def workout(request):
    '''
    User scenario: Let the user see the previous works and provide
    and initial way to create new workouts.
    '''
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout_model = form.save(commit=False)
            workout_model.user_fk = request.user
            workout_model.save()
            return HttpResponseRedirect('/workout/')
    else:
        form = WorkoutForm()  # An unbound form

    # TODO - do we want a CBV to paginate the workouts?
    # List the available workouts
    workouts = Workout.objects.filter(user_fk=request.user)

    return render(request, 'mainapp/workout.html', {
        'form': form,
        'workouts': workouts,
    })


@login_required(login_url='/accounts/signin/')
def workout_detail(request, pk):
    '''
    User scenario: Let the user add workoutsets (exercise with rep count
    and weights) to the given workout.
    '''
    workout = get_object_or_404(Workout, pk=pk)
    if workout.user_fk != request.user:
        raise Http404

    if request.method == 'POST':
        form = WorkoutSetForm(request.POST)
        if form.is_valid():

            # The transaction is used for incrementing the order column
            # https://docs.djangoproject.com/en/dev/topics/db/transactions/
            with transaction.atomic():
                workout_set_model = form.save(commit=False)
                workout_set_model.workout_fk = workout
                workout_set_model.order = WorkoutSet.objects.filter(workout_fk=workout.id).order_by("-order")[0].order + 1
                workout_set_model.save()
            # TODO - fix redirect link
            return HttpResponseRedirect('/workout_detail/' + str(workout.id) + "/#addworkout")
    else:
        form = WorkoutSetForm()

    workout_sets = WorkoutSet.objects.filter(workout_fk=workout.id).select_related("exercise_fk").order_by("order")
    # convert to user's preference of weight format
    # http://stackoverflow.com/questions/2115869/calling-python-function-in-django-template
    user_profile = request.user.user_profile

    for w_set in workout_sets:
        # Generate the weight we will display to the user.
        setattr(w_set, 'user_weight_value', getattr(w_set.weight, w_set.weight_unit))

    return render(request, 'mainapp/workout_detail.html', {
        'form': form,
        'workout': workout,
        'workout_sets': workout_sets,
        'user_profile': user_profile,
    })
