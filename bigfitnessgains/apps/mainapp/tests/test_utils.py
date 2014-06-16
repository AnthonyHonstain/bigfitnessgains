from django.utils import timezone
from django.contrib.auth import models as core_models

from bigfitnessgains.apps.mainapp import models
from bigfitnessgains.apps.accounts import models as userena_models


def setup_database():
    ''' set up a few muscle groups, exercises, some workouts and some sets for a workout
    '''
    user = core_models.User.objects.create_user('atestuser', 'test@test.com', 'atestpassword')
    profile = userena_models.UserProfile.objects.create(user=user)

    _create_muscle_group("Arms")
    _create_muscle_group("Legs")
    _create_muscle_group("Brain")
    muscle_group_fks = models.MuscleGroup.objects.all()

    _create_exercise("Truck Pull", muscle_group_fks[:len(muscle_group_fks) - 1])
    _create_exercise("Caber Toss", muscle_group_fks)

    _create_workout(user, "Leg day", timezone.now())
    _create_workout(user, "Also leg day", timezone.now())
    _create_workout(user, "Erry day is leg day", timezone.now())

    leg_exercise = models.Exercise.objects.get(exercise_name="Truck Pull")
    leg_workout = models.Workout.objects.get(user_fk=user, workout_name="Erry day is leg day")
    
    _create_workout_set(leg_workout, leg_exercise, 12)
    _create_workout_set(leg_workout, leg_exercise, 10)
    _create_workout_set(leg_workout, leg_exercise, 8)


def _create_exercise(name, muscle_group_fks):
    new = models.Exercise.objects.create(exercise_name=name)
    for fk in muscle_group_fks:
        models.ExerciseToMuscleGroup.objects.create(exercise_fk=new,
                                                    muscle_group_fk=fk,
                                                    is_primary=False)


def _create_muscle_group(name):
    models.MuscleGroup.objects.create(muscle_group_name=name)


def _create_workout(user, workout_name, workout_date=timezone.now()):
    models.Workout.objects.create(user_fk=user,
                                workout_name=workout_name,
                                workout_date=workout_date)

# TODO: figure out how django-measurement fetches the Weight(g)
# to dump into column and use that here, instead of a string
def _create_workout_set(workout_fk, exercise_fk, reps=5, weight=100, weight_unit='kg', weight_measure='Weight(g)'):
    models.WorkoutSet.objects.create(workout_fk=workout_fk,
                                    exercise_fk=exercise_fk,
                                    reps=reps,
                                    weight_value=weight,
                                    weight_unit=weight_unit,
                                    weight_measure=weight_measure)






