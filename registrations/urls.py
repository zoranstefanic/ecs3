from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'form/$', views.RegistrationCreate.as_view(), name='registration_form'),
    url(r'update/(?P<pk>\d+)$', views.RegistrationUpdate.as_view(), name='registration_update'),
    url(r'accept/(?P<pk>\d+)$', views.registration_accept, name='registration_accept'),
    url(r'accepted/(?P<pk>\d+)$', views.registration_accepted, name='registration_accepted'),
    url(r'list/$', views.RegistrationList.as_view(), name='registration_list'),
    url(r'thanks/$', views.thanks, name='thanks')
]
