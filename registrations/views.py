from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib import messages
from .forms import RegistrationForm
from .models import Registration


SENDER = 'registration@htcc2018.org'
HOTEL_EMAILS = ['valentina.zarkovic@bluesunhotels.com','antonija.brlek@bluesunhotels.com']

class RegistrationCreate(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/registration/register/thanks/"

    def form_valid(self, form):
        form.send_email()
        return super(RegistrationCreate, self).form_valid(form)

def thanks(request):
    return render(request,'thanks.html')

def home(request):
    return redirect('/')

class RegistrationList(ListView):
    model = Registration
    template_name = "registration_list.html"

class RegistrationListPaid(ListView):
    model = Registration
    template_name = "registration_list.html"
    queryset = Registration.objects.filter(paid=True) 

class RegistrationUpdate(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'registration_update.html'
    success_url = "/registration/register/list/"

@login_required
def registration_accept(request,pk):
    reg = Registration.objects.get(pk=pk)
    return render(request,'registration_accept.html',{'reg':reg})

@login_required
def registration_accepted(request,pk):
    reg = Registration.objects.get(pk=pk)
    reg.accepted = True
    reg.save()
    send_accept_email(reg)
    messages.add_message(request, messages.SUCCESS, 'Acceptance email was sent to: %s!.' % reg.email)
    return redirect('registration_list')

@login_required
def registration_pay(request,pk):
    reg = Registration.objects.get(pk=pk)
    return render(request,'registration_pay.html',{'reg':reg})

@login_required
def registration_paid(request,pk):
    reg = Registration.objects.get(pk=pk)
    reg.paid = True
    reg.save()
    paid_email_user(reg)
    paid_email_hotel(reg,HOTEL_EMAILS)
    paid_email_hotel(reg,[SENDER])
    messages.add_message(request, messages.SUCCESS, 'Email was sent to: %s and to the hotel!.' % reg.email)
    return redirect('registration_list')

def send_accept_email(reg):
    subject = 'Hot topics in contemporary crystallography 2018 acceptance'
    from_email = SENDER
    text_content = render_to_string('emails/accept_email.txt', {"reg":reg})
    html_content = render_to_string('emails/accept_email.html', {"reg":reg})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [reg.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print "Email sent to: %s" %reg.email

def paid_email_user(reg):
    """ Send an email to user confirming her/his payment """

    subject = 'Registration for HTCC2018 number %s is paid' % reg.code
    from_email = SENDER
    text_content = render_to_string('emails/paid_email_user.txt', {"reg":reg})
    html_content = render_to_string('emails/paid_email_user.html', {"reg":reg})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [reg.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print "Email sent to: %s" %reg.email

def paid_email_hotel(reg,emails):
    """ Send an email to hotel with the data needed for the accommodation"""

    subject = 'Registration at HTCC2018 n. %s is paid' % reg.code
    from_email = SENDER
    text_content = render_to_string('emails/paid_email_hotel.txt', {"reg":reg})
    html_content = render_to_string('emails/paid_email_hotel.html', {"reg":reg})
    msg = EmailMultiAlternatives(subject, text_content, from_email, emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print "Email sent to: %s" % emails
