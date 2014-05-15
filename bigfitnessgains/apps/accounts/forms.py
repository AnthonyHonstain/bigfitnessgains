from userena.utils import get_profile_model
from userena.forms import EditProfileForm


class EditProfileFormExtra(EditProfileForm):
    '''
    The whole purpose of this is also exclude mugshot, we
    don't want tackle integrating that with our AWS storage
    at this stage. 5/14/2014
    '''

    class Meta:
        model = get_profile_model()
        exclude = ['user', 'mugshot']
