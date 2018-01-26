from random import choice
from django.db import models

MODULECHOICES = ((1, 'Single crystal diffraction'),
                 (2, 'Powder diffraction'))

STATUSCHOICES = ((1, 'student'),
                 (2, 'lecturer'),
                 (3, 'accompanying person'),
                 (4, 'organizer'),
                 (5, 'sponsor representative'))

TITLECHOICES = ((1, 'Mr.'),
                 (2, 'Ms.'),
                 (3, 'Dr.'),
                 (4, 'Prof.'))

HOTELCHOICES = ((1, '3***'),
                 (2, '4****'),
                 )
ROOMCHOICES = ((1, 'shared double room'),
                 (2, 'double room single use'),
                 )
EXPERTISE_CHOICES = ((1, 'beginner'),
                 (2, 'intermediate'),
                 (3, 'advanced'),
                 )

def generate_code():
    "This has to insure to pick a unique number from remaining"
    taken_codes = set(Registration.objects.values_list('code',flat=True))
    available_codes = set(range(1,999)) - taken_codes 
    return choice(list(available_codes))

class Registration(models.Model):
    "Stores registration and payment information"

    # General information
    title = models.IntegerField(choices=TITLECHOICES, default=1)
    name = models.CharField(max_length=50, verbose_name="Name")
    surname = models.CharField(max_length=50, verbose_name="Surname")
    email = models.EmailField(max_length=50, unique=True)
    date_of_birth = models.DateField(verbose_name="Date of birth")
    affiliation = models.CharField(max_length=200,verbose_name="Affiliation")
    address = models.CharField(max_length=100)

    #module = models.IntegerField(choices=MODULECHOICES)
    status = models.IntegerField(choices=STATUSCHOICES, verbose_name="Status at HTCC2018")
    #Bursaries
    bursary  = models.BooleanField(default=False, help_text="I would like to apply for bursary")
    cv = models.FileField(upload_to="bursaries",
                            verbose_name = "Curriculum vitae",
                            blank=True, null=True, 
                            help_text="Upload your CV.")
    mot_letter = models.FileField(upload_to="bursaries",
                            verbose_name = "Motivation letter",
                            blank=True, null=True, 
                            help_text="Upload your motivation letter.")
    rec_letter = models.FileField(upload_to="bursaries",
                            verbose_name = "Recommandation letter",
                            blank=True, null=True, 
                            help_text="Upload your recommendation letter.")

    # Accommodation details
    hotel_category = models.IntegerField(choices=HOTELCHOICES, default=1)
    room_choice = models.IntegerField(choices=ROOMCHOICES, default=1)
    room_preference = models.CharField(max_length=50, verbose_name="I would like to share the room with", null=True, blank=True)
    arrival     = models.DateField(verbose_name="Date of arrival", default="2018-09-23")
    departure   = models.DateField(verbose_name="Date of departure", default="2018-09-27")

    accepted = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    paid = models.BooleanField(default=False, editable=False)
    code = models.PositiveSmallIntegerField(editable=False, default = generate_code)

    topic1_expertise = models.IntegerField(verbose_name="Hot topic 1 (Extreme conditions) expertise",
                                          choices=EXPERTISE_CHOICES,
                                          help_text="How would your rate your expertise in Hot topic 1: Extreme conditions",     
                                          default=1)
    topic2_expertise = models.IntegerField(verbose_name="Hot topic 2 (Total scattering and PDF analysis of complex materials) expertise",
                                          choices=EXPERTISE_CHOICES,
                                          help_text="How would your rate your expertise in Hot topic 2: Total scattering and PDF analysis of complex materials"      ,
                                          default=1)
    topic3_expertise = models.IntegerField(verbose_name="Hot topic 3 (Dynamical crystallography) expertise",
                                          choices=EXPERTISE_CHOICES,
                                          help_text="How would your rate your expertise in Hot topic 3: Dynamical crystallography",
                                           default=1)
    
    
    def __unicode__(self):
       return '%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['-created']

