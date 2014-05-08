from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='user_profile')
    location_country = models.CharField(_('country'),
                                    max_length=60)
    fitness_focus = models.CharField(_('fitness focus'),
                                    max_length=60)
    # really just to see if anybody fills this out
    spirit_animal = models.CharField(_('spirit animal'),
                                    max_length=60)
