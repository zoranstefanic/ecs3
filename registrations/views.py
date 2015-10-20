from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import RegistrationForm
from .models import Registration


class RegistrationCreate(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/registration/thanks/"

    def form_valid(self, form):
        form.send_email()
        return super(RegistrationCreate, self).form_valid(form)

def thanks(request):
    return render(request,'thanks.html')

def home(request):
    return render(request,'home.html')

class RegistrationList(ListView):
    model = Registration
    template_name = "registration_list.html"
