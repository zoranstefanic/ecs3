from django.forms import ModelForm
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from django.core.mail import send_mail
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

    def send_email(self):
        # send email using the self.cleaned_data dictionary
	text = str(self.cleaned_data)
        send_mail('Testing of ECS3 email', text, settings.DEFAULT_FROM_EMAIL,
        ['zoran.stefanic@irb.hr'], fail_silently=False)

    
