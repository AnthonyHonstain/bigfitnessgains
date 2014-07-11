from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.contrib.auth import models as core_models

from bigfitnessgains.apps.accounts import models as acc_models

from bigfitnessgains.apps.mainapp import models
from bigfitnessgains.apps.mainapp import views
from bigfitnessgains.apps.mainapp.tests.test_utils import setup_database


class TestWorkoutDetail(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        setup_database()

    ## https://docs.djangoproject.com/en/1.5/topics/testing/advanced/
    def test_workout_set_display_profile(self):
        workouts = models.Workout.objects.all()
        w_pk = workouts[0].id
        request = self.factory.get('/workout_detail/{0}/'.format(w_pk))

        user = core_models.User.objects.get(username='atestuser')
        request.user = user

        resp = views.workout_detail(request, w_pk)

        self.assertEqual(resp.status_code, 200)

        # switch user profile to kg
        profile = acc_models.UserProfile.objects.get(user=user)
        profile.weight_unit = 'kg'
        profile.save()

        request = self.factory.get('/workout_detail/{0}/'.format(w_pk))
        user = core_models.User.objects.get(username='atestuser')
        request.user = user
        resp = views.workout_detail(request, w_pk)

        self.assertEqual(resp.status_code, 200)
