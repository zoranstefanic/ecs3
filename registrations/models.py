from random import choice
from django.db import models

MODULECHOICES = ((1, 'Single crystal diffraction'),
                 (2, 'Powder diffraction'))

STATUSCHOICES = ((1, 'young academic'),
                 (5, 'senior academic'),
                 (6, 'non-academic'),
                 (2, 'lecturer'),
                 (3, 'accompanying person'),
                 (4, 'organizer'))

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

    module = models.IntegerField(choices=MODULECHOICES)
    status = models.IntegerField(choices=STATUSCHOICES, verbose_name="Status at ECS3")
    abstract = models.FileField(upload_to="abstracts",
                            blank=True, null=True, 
                            help_text="Upload your abstract.")

    # Accommodation details
    hotel_category = models.IntegerField(choices=HOTELCHOICES, default=1)
    room_choice = models.IntegerField(choices=ROOMCHOICES, default=1)
    room_preference = models.CharField(max_length=50, verbose_name="I would like to share the room with", null=True, blank=True)
    arrival     = models.DateField(verbose_name="Date of arrival", default="2016-09-25")
    departure   = models.DateField(verbose_name="Date of departure", default="2016-10-02")

    full_board  = models.BooleanField(default=False, help_text="")
    lunch_box   = models.BooleanField(default=False)

    accepted = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    paid = models.BooleanField(default=False, editable=False)
    code = models.PositiveSmallIntegerField(editable=False, default = generate_code)
    
    def __unicode__(self):
       return '%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['-created']

