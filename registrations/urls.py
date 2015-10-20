from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'form/$', views.RegistrationCreate.as_view(), name='registration_form'),
    url(r'list/$', views.RegistrationList.as_view(), name='registration_list'),
    url(r'thanks/$', views.thanks, name='thanks')
]
