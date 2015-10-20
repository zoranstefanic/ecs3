from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from .models import Registration

YEAR_CHOICES = range(2015-80, 2001)
YEAR_CHOICES.reverse()


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'surname': forms.TextInput(
                attrs={'placeholder': 'Your surname'}),
            'date_of_birth': SelectDateWidget(years= YEAR_CHOICES),
            'arrival': SelectDateWidget(months= {9:'September',10:"October"}, years=['2016']),
            'departure': SelectDateWidget(months= {9:'September',10:"October"}, years=['2016']),
        }
