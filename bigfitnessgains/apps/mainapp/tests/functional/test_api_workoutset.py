from datetime import datetime
from django.utils.timezone import utc
import random

import json
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.contrib.auth import models as core_models

from bigfitnessgains.apps.mainapp import models
from bigfitnessgains.apps.accounts import models as userena_models

# http://www.django-rest-framework.org/api-guide/testing#authenticating
from rest_framework.test import APIClient


class TestWorkoutSetAPI(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.user = core_models.User.objects.create_user('atestuser', 'test@test.com', 'atestpassword')
        profile = userena_models.UserProfile.objects.create(user=self.user)

        self.user_2 = core_models.User.objects.create_user('atestuser2', 'test2@test.com', 'atestpassword2')
        profile = userena_models.UserProfile.objects.create(user=self.user_2)

        self.group_arms = models.MuscleGroup.objects.create(muscle_group_name="Arms")
        self.group_legs = models.MuscleGroup.objects.create(muscle_group_name="Legs")
        self.group_brain = models.MuscleGroup.objects.create(muscle_group_name="Brain")

        self.exercise_truck = self._create_exercise("Truck Pull", [self.group_legs, ])
        self.exercise_caber = self._create_exercise("Caber Toss", [self.group_arms,
                                                                   self.group_brain])
        # http://www.django-rest-framework.org/api-guide/testing#authenticating
        self.client = APIClient()

    def _create_exercise(self, name, muscle_group_fks):
        new = models.Exercise.objects.create(exercise_name=name)
        for fk in muscle_group_fks:
            models.ExerciseToMuscleGroup.objects.create(exercise_fk=new,
                                                        muscle_group_fk=fk,
                                                        is_primary=False)
        return new

    def test_workout_set_get(self):
        '''Test WorkoutSet GET for a given workout (with and without WorkoutSets)'''
        self.client.login(username='atestuser', password='atestpassword')

        rand_workout = 'Test_workout_' + str(random.randint(0, 100))
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name=rand_workout,
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Check the GET endpoint when the Workout has no WorkoutSet
        resp = self.client.get('/workouts/{0}/workoutsets/'.format(workout.id))
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)
        # There should be no WorkoutSet for this Workout yet.
        self.assertEqual(len(json_body), 0)

        # Add a single WorkoutSet
        models.WorkoutSet.objects.create(workout_fk=workout,
                                         exercise_fk=self.exercise_caber,
                                         reps=1,
                                         order=1,
                                         weight_value=100,
                                         weight_unit='lb',
                                         weight_measure='Weight(g)')

        resp = self.client.get('/workouts/{0}/workoutsets/'.format(workout.id))
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)
        self.assertEqual(len(json_body), 1)
        self.assertEqual(json_body[0]['workout_fk']['workout_name'],
                         rand_workout)
        self.assertEqual(json_body[0]['reps'], 1)

    def test_workout_set_get_perm(self):
        '''Test WorkoutSet GET to verify you can't access someone else's Workout'''
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name='test workout',
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Verify that user two can't access the workout
        self.client.login(username='atestuser2', password='atestpassword2')

        # Check the GET endpoint when the Workout has no WorkoutSet
        resp = self.client.get('/workouts/{0}/workoutsets/'.format(workout.id))
        self.assertEqual(resp.status_code, 403)

    def test_workout_set_post(self):
        '''Test WorkoutSet POST for a given workout (with and without WorkoutSets)'''
        self.client.login(username='atestuser', password='atestpassword')

        # Manually create a new workout.
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name="Test workout",
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        exercise = models.Exercise.objects.get(exercise_name='Caber Toss')

        # Use the POST endpoint to create a few WorkoutSets
        data = {'workout_fk': workout.id,
                'exercise_fk': exercise.id,
                'reps': 1,
                'order': 1,
                'weight_0': 1,
                'weight_1': 'kg'
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 200)
        set_one = json.loads(resp.content)

        data = {'workout_fk': workout.id,
                'exercise_fk': exercise.id,
                'reps': 2,
                'order': 2,
                'weight_0': 2,
                'weight_1': 'kg'
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 200)
        set_two = json.loads(resp.content)

        # Sanity check the data in the database.
        workoutset_all = models.WorkoutSet.objects.all()
        for test_workoutset in workoutset_all:
            self.assertEqual(test_workoutset.workout_fk.id, workout.id)
            self.assertEqual(test_workoutset.exercise_fk.id, exercise.id)
        self.assertEqual(set_one['reps'], workoutset_all[0].reps)
        self.assertEqual(set_two['reps'], workoutset_all[1].reps)

    def test_workout_set_post_perm(self):
        '''Test WorkoutSet POST to verify you can't POST to someone else's Workout'''
        # Manually create a new workout.
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name="Test workout",
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        exercise = models.Exercise.objects.get(exercise_name='Caber Toss')

        # Verify that user two can't access the workout
        self.client.login(username='atestuser2', password='atestpassword2')

        data = {'workout_fk': workout.id,
                'exercise_fk': exercise.id,
                'reps': 1,
                'order': 1,
                'weight_0': 1,
                'weight_1': 'kg'
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 403)

    def test_workout_set_get_detail(self):
        '''Test WorkoutSet GET for a given workout (with and without WorkoutSets)'''
        self.client.login(username='atestuser', password='atestpassword')

        rand_int = random.randint(0, 100)
        rand_workout = 'Test_workout_' + str(rand_int)
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name=rand_workout,
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Add a single WorkoutSet
        workoutset = models.WorkoutSet.objects.create(workout_fk=workout,
                                                      exercise_fk=self.exercise_caber,
                                                      reps=rand_int,
                                                      order=rand_int,
                                                      weight_value=100,
                                                      weight_unit='lb',
                                                      weight_measure='Weight(g)')

        resp = self.client.get('/workouts/{0}/workoutsets/{1}/'.format(workout.id, workoutset.id))
        self.assertEqual(resp.status_code, 200)
        json_body = json.loads(resp.content)

        self.assertEqual(json_body['workout_fk']['workout_name'],
                         rand_workout)
        self.assertEqual(json_body['reps'], rand_int)
        self.assertEqual(json_body['order'], rand_int)
