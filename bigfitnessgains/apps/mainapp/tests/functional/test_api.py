import json
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.contrib.auth import models as core_models

from bigfitnessgains.apps.mainapp import models
from bigfitnessgains.apps.mainapp.tests.test_utils import setup_database


class TestExerciseAPI(TestCase):

    def setUp(self):
        self.client = Client()
        setup_database()

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
        setup_database()

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
        self.factory = RequestFactory()
        setup_database()

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
                'order' : 1,
                'weight_0': 100,
                'weight_1': 'kg'
                }
        ## next, test POSTS with only LB or only KG
        resp = self.client.post('/workout_sets/', data)
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)
        ## assert we've returned a new id for the new record
        self.assertTrue(isinstance(json_body.get('id', None), int))
