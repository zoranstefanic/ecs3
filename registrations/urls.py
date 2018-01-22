from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #url(r'^home/$', views.home, name='home'),
    url(r'^form/$', views.RegistrationCreate.as_view(), name='registration_form'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    # Below are the login protected views
    url(r'^list/$', login_required(views.RegistrationList.as_view()), name='registration_list'),
    url(r'^list_paid/$', login_required(views.RegistrationListPaid.as_view()), name='registration_list_paid'),
    url(r'^update/(?P<pk>\d+)$', login_required(views.RegistrationUpdate.as_view()), name='registration_update'),
    url(r'^accept/(?P<pk>\d+)$', views.registration_accept, name='registration_accept'),
    url(r'^accepted/(?P<pk>\d+)$', views.registration_accepted, name='registration_accepted'),
    url(r'^pay/(?P<pk>\d+)$', views.registration_pay, name='registration_pay'),
    url(r'^paid/(?P<pk>\d+)$', views.registration_paid, name='registration_paid'),
]
