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
            'arrival': SelectDateWidget(months= {4:'April'}, years=['2017']),
            'departure': SelectDateWidget(months= {4:'April'}, years=['2017']),
        }

    #def clean_abstract(self):
    #    "Do not allow empty abstract field if status is young academic"
        # Ovo smo poslije ukinuli!
        
    #    status = self.cleaned_data['status']
    #    if status == 1 and not self.cleaned_data['abstract']:
    #        raise forms.ValidationError("You must upload an abstract if you are a young academic!")        
    #    
    #    return self.cleaned_data['abstract']


    def clean_departure(self):
        "Departure must come after arrival"
        
        arrival = self.cleaned_data['arrival']
        departure = self.cleaned_data['departure']
        if departure <= arrival:
            raise forms.ValidationError("Departure date must come after arrival date!")
        
        return self.cleaned_data['departure']

    def send_email(self):
        message = "New registration for HTCC2017 was created. See at http://ecs3.ecanews.org/registration/list/"
        send_mail('New registration for HTCC2017 was created', message, settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL], fail_silently=False)

    
