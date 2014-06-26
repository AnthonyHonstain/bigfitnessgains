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

        # Use the POST endpoint to create a few WorkoutSets
        data = {'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': 5,
                'order': 5,
                'user_weight_value': 100,
                'weight_unit': 'kg',
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 200, resp.content)
        set_one = json.loads(resp.content)

        # -------------------------------------------
        # Verify the serializer
        # -------------------------------------------
        # NOTE - we expect the workout_fk and exercise_fk to contain their
        # respective models (and not just be a foreign key id).
        self.assertEqual(set_one['workout_fk']['id'], workout.id)
        self.assertEqual(set_one['exercise_fk']['id'], self.exercise_caber.id)

        # Warning - watch out for the special logic on weight_* fields
        self.assertEqual(set_one['weight_value'], 100000)
        self.assertEqual(set_one['user_weight_value'], 100)
        self.assertEqual(set_one['weight_unit'], 'kg')
        self.assertEqual(set_one['weight_measure'], 'Weight(g)')
        self.assertEqual(set_one['order'], 5)

        # -------------------------------------------
        # Verify the data in the database
        # -------------------------------------------
        workoutset_all = models.WorkoutSet.objects.all()
        self.assertEqual(len(workoutset_all), 1)
        test_workoutset = workoutset_all[0]

        self.assertEqual(test_workoutset.workout_fk.id, workout.id)
        self.assertEqual(test_workoutset.exercise_fk.id, self.exercise_caber.id)
        self.assertEqual(test_workoutset.reps, 5)
        self.assertEqual(test_workoutset.order, 5)
        self.assertEqual(test_workoutset.weight_value, 100000)
        self.assertEqual(test_workoutset.weight_unit, 'kg')
        self.assertEqual(test_workoutset.weight_measure, 'Weight(g)')

    def test_workout_set_post_multiple(self):
        '''Test WorkoutSet POST for a given workout (with and without WorkoutSets)'''
        self.client.login(username='atestuser', password='atestpassword')

        # Manually create a new workout.
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name="Test workout",
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Use the POST endpoint to create a few WorkoutSets
        data = {'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': 1,
                'order': 1,
                'user_weight_value': 1,
                'weight_unit': 'kg',
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 200)
        set_one = json.loads(resp.content)

        data = {'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': 2,
                'order': 2,
                'user_weight_value': 2,
                'weight_unit': 'kg',
                }
        resp = self.client.post('/workouts/{0}/workoutsets/'.format(workout.id), data)
        self.assertEqual(resp.status_code, 200)
        set_two = json.loads(resp.content)

        # Sanity check the data in the database.
        workoutset_all = models.WorkoutSet.objects.all()
        for test_workoutset in workoutset_all:
            self.assertEqual(test_workoutset.workout_fk.id, workout.id)
            self.assertEqual(test_workoutset.exercise_fk.id, self.exercise_caber.id)
        self.assertEqual(set_one['reps'], workoutset_all[0].reps)
        self.assertEqual(set_two['reps'], workoutset_all[1].reps)

    def test_workout_set_post_perm(self):
        '''Test WorkoutSet POST to verify you can't POST to someone else's Workout'''
        # Manually create a new workout.
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name="Test workout",
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Verify that user two can't access the workout
        self.client.login(username='atestuser2', password='atestpassword2')

        data = {'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': 1,
                'order': 1,
                'user_weight_value': 1,
                'weight_unit': 'kg',
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

    def test_workout_set_put_delete(self):
        '''Test WorkoutSet PUT for a given workout'''
        self.client.login(username='atestuser', password='atestpassword')

        rand_int = random.randint(0, 100)
        rand_workout = 'Test_workout_' + str(rand_int)
        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name=rand_workout,
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        workout_2 = models.Workout.objects.create(user_fk=self.user,
                                                  workout_name='Secondary Workout',
                                                  workout_date=datetime.utcnow().replace(tzinfo=utc))

        # Add a single WorkoutSet
        workoutset = models.WorkoutSet.objects.create(workout_fk=workout,
                                                      exercise_fk=self.exercise_caber,
                                                      reps=rand_int,
                                                      order=rand_int,
                                                      weight_value=100,
                                                      weight_unit='lb',
                                                      weight_measure='Weight(g)')

        # Validate that we can't change the workout the workoutset it attached to.
        data = {'id': workoutset.id,
                'workout_fk': workout_2.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': rand_int + 1,
                'order': rand_int + 1,
                'user_weight_value': 1,
                'weight_unit': 'kg',
                }
        resp = self.client.put('/workouts/{0}/workoutsets/{1}/'
                                ''.format(workout.id, workoutset.id), data)
        self.assertEqual(resp.status_code, 200)
        # We are really concerned with making sure the value didn't change in the DB.
        self.assertEqual(models.WorkoutSet.objects.get(pk=workoutset.id).workout_fk.id,
                         workout.id)

        # Use the PUT to update the workoutset
        data = {'id': workoutset.id,
                'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': rand_int + 1,
                'order': rand_int + 1,
                'user_weight_value': 1,
                'weight_unit': 'kg',
                }
        resp = self.client.put('/workouts/{0}/workoutsets/{1}/'
                                ''.format(workout.id, workoutset.id), data)
        self.assertEqual(resp.status_code, 200)
        #set_one = json.loads(resp.content)

        # Sanity check the data in the database.
        workoutset_all = models.WorkoutSet.objects.all()
        self.assertEqual(len(workoutset_all), 1)

        self.assertEqual(workoutset_all[0].id, workoutset.id)
        self.assertEqual(workoutset_all[0].workout_fk.id, workout.id)
        self.assertEqual(workoutset_all[0].exercise_fk.id, self.exercise_caber.id)
        self.assertEqual(workoutset_all[0].reps, rand_int + 1)
        self.assertEqual(workoutset_all[0].order, rand_int + 1)

        # Delete the record we updated
        resp = self.client.delete('/workouts/{0}/workoutsets/{1}/'
                                  ''.format(workout.id, workoutset.id))
        self.assertEqual(resp.status_code, 204)

        # Sanity check the data in the database.
        workoutset_all = models.WorkoutSet.objects.all()
        self.assertEqual(len(workoutset_all), 0)

    def test_workout_set_put_delete_perm(self):
        '''Test WorkoutSet GET, PUT, DELETE permissions'''

        workout = models.Workout.objects.create(user_fk=self.user,
                                                workout_name='Test Workout Permissions',
                                                workout_date=datetime.utcnow().replace(tzinfo=utc))

        workoutset = models.WorkoutSet.objects.create(workout_fk=workout,
                                                      exercise_fk=self.exercise_caber,
                                                      reps=1,
                                                      order=1,
                                                      weight_value=100,
                                                      weight_unit='lb',
                                                      weight_measure='Weight(g)')

        # Access the REST endpoints as a different user (than created the workout)
        self.client.login(username='atestuser2', password='atestpassword2')

        # Validate we can't GET someone else's workoutset
        resp = self.client.get('/workouts/{0}/workoutsets/{1}/'.format(workout.id, workoutset.id))
        self.assertEqual(resp.status_code, 403)

        # Validate we can't PUT / update someone else's workoutset
        data = {'id': workoutset.id,
                'workout_fk': workout.id,
                'exercise_fk': self.exercise_caber.id,
                'reps': 2,
                'order': 2,
                'user_weight_value': 1,
                'weight_unit': 'kg',
                }
        resp = self.client.put('/workouts/{0}/workoutsets/{1}/'
                                ''.format(workout.id, workoutset.id), data)
        self.assertEqual(resp.status_code, 403)

        # Validate we can't DELETE someone else's workoutset
        resp = self.client.delete('/workouts/{0}/workoutsets/{1}/'
                                  ''.format(workout.id, workoutset.id))
        self.assertEqual(resp.status_code, 403)
