from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
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

class RegistrationUpdate(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'registration_update.html'
    success_url = "/registration/list/"

def registration_accept(request,pk):
    reg = Registration.objects.get(pk=pk)
    return render(request,'registration_accept.html',{'reg':reg})

def registration_accepted(request,pk):
    reg = Registration.objects.get(pk=pk)
    reg.accepted = True
    reg.save()
    return redirect('registration_list')
