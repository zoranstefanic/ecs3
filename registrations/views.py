from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import RegistrationForm
from .models import Registration


class RegistrationCreate(CreateView):
    model = Registration
    template_name = "register.html"
    success_url = "/registration/thanks/"
    fields = ['title','name','surname','email', 'date_of_birth', 
               'affiliation', 'address', 'module', 'status', 'abstract',
               'room_choice', 'room_preference', 'arrival', 'departure',
                'full_board', 'lunch_box']

def thanks(request):
    return render(request,'thanks.html')

def home(request):
    return render(request,'home.html')
