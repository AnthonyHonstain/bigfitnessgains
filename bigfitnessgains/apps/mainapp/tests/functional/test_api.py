import json
from django.utils import timezone
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import models as core_models
from bigfitnessgains.apps.mainapp import models

class TestExerciseAPI(TestCase):

    def setUp(self):
        self.client = Client()
        _setup_database()

    def test_exercise_list_api(self):
        resp = self.client.get('/exercise/')
        self.assertEqual(resp.status_code, 200)
        
    def test_exercise_detail_api(self):
        exercises = models.Exercise.objects.all()
        exer_pk = exercises[0].id
        resp = self.client.get('/exercise/{0}/'.format(exer_pk))
        self.assertEqual(resp.status_code, 200)
        
    def test_exercise_post_api(self):
        ### not supported yet
        pass


class TestWorkoutAPI(TestCase):

    def setUp(self):
        self.client = Client()
        _setup_database()

    def test_workout_list_api(self):
        resp = self.client.get('/workouts/')
        self.assertEqual(resp.status_code, 200)

    def test_workout_detail_api(self):
        workouts = models.Workout.objects.all()
        workout_pk = workouts[0].id
        resp = self.client.get('/workouts/{0}/'.format(workout_pk))
        self.assertEqual(resp.status_code, 200)

    def test_workout_post_api(self):
        user = core_models.User.objects.get(username='atestuser')
        data = { 'user_fk' : user.id,
                'workout_name' : 'Yet another leg day joke',
                'workout_date' : '2014-01-01T12:00+08:00'}
        resp = self.client.post('/workouts/', data)
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)
        ## assert we've returned a new id for the new record
        self.assertTrue(isinstance(json_body.get('id', None), int))


class TestWorkoutSetAPI(TestCase):

    def setUp(self):
        self.client = Client()
        _setup_database()

    def test_workout_set_list_api(self):
        resp = self.client.get('/workout_sets/')
        self.assertEqual(resp.status_code, 200)

    def test_workout_set_detail_api(self):
        sets = models.WorkoutSet.objects.all()
        set_pk = sets[0].id
        resp = self.client.get('/workout_sets/{0}/'.format(set_pk))
        self.assertEqual(resp.status_code, 200)

    def test_workout_set_post_api(self):
        user = core_models.User.objects.get(username='atestuser')
        leg_workout = models.Workout.objects.get(user_fk=user, workout_name="Erry day is leg day")
        exercise = models.Exercise.objects.get(exercise_name='Caber Toss')
        data = { 'workout_fk' : leg_workout.id,
                'exercise_fk' : exercise.id,
                'reps' : 10,
                'weight_lb' : 100,
                'weight_kg' : 45}
        ## next, test POSTS with only LB or only KG
        resp = self.client.post('/workout_sets/', data)
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)
        ## assert we've returned a new id for the new record
        self.assertTrue(isinstance(json_body.get('id', None), int))

def _setup_database():
    ''' set up a few muscle groups, exercises, some workouts and some sets for a workout
    '''
    user = core_models.User.objects.create_user('atestuser', 'test@test.com', 'atestpassword')

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


def _create_workout_set(workout_fk, exercise_fk, reps=5, weight_lb=100, weight_kg=45):
    models.WorkoutSet.objects.create(workout_fk=workout_fk,
                                    exercise_fk=exercise_fk,
                                    reps=reps,
                                    weight_lb=weight_lb,
                                    weight_kg=weight_kg)






