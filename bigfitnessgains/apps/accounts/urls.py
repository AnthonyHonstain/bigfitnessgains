from django.conf.urls import patterns, include, url

from forms import EditProfileFormExtra


urlpatterns = patterns('',

    url(r'^(?P<username>[\.\w-]+)/edit/$',
        'userena.views.profile_edit',
        {'edit_profile_form': EditProfileFormExtra},
        name='edit-profile'),

    url(r'^', include('userena.urls')),

)
