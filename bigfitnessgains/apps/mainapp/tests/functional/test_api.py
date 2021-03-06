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
