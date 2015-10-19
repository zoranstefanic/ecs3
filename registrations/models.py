from random import randint
from django.db import models

MODULECHOICES = ((1, 'Single crystal diffraction'),
                 (2, 'Powder diffraction'))

STATUSCHOICES = ((1, 'participant'),
                 (2, 'lecturer'),
                 (3, 'accompanying person'))

TITLECHOICES = ((1, 'Mr.'),
                 (2, 'Ms.'),
                 (3, 'Dr.'))

HOTELCHOICES = ((1, '3***'),
                 (2, '4****'),
                 )
ROOMCHOICES = ((1, 'shared double room'),
                 (2, 'double room single use'),
                 )

def generate_code():
    i = randint(1,999)
    return i

class Registration(models.Model):
    "Stores registration and payment information"

    # General information
    title = models.IntegerField(choices=TITLECHOICES, default=1)
    name = models.CharField(max_length=50, verbose_name="Name")
    surname = models.CharField(max_length=50, verbose_name="Surname")
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField(verbose_name="Date of birth", help_text="Format yyyy-mm-dd")
    affiliation = models.CharField(max_length=200,verbose_name="Affiliation")
    address = models.CharField(max_length=100)

    module = models.IntegerField(choices=MODULECHOICES)
    status = models.IntegerField(choices=STATUSCHOICES, verbose_name="Status at ECS3")
    abstract = models.FileField(blank=True, null=True, help_text="Only participants need to upload an abstract")

    # Accommodation details
    hotel_category = models.IntegerField(choices=HOTELCHOICES, default=1)
    room_choice = models.IntegerField(choices=ROOMCHOICES, default=1)
    room_preference = models.CharField(max_length=50, verbose_name="I would like to share the room with", null=True, blank=True)
    arrival     = models.DateField(verbose_name="Date of arrival", default="2016-09-25", help_text="Format dd-mm-yyyy")
    departure   = models.DateField(verbose_name="Date of departure", default="2016-10-02", help_text="Format dd-mm-yyyy")

    full_board  = models.BooleanField(default=False, help_text="")
    lunch_box   = models.BooleanField(default=False)

    accepted = models.NullBooleanField(editable=False)
    paid = models.NullBooleanField(editable=False)
    code = models.PositiveSmallIntegerField(editable=False, default = generate_code)
    
    def __unicode__(self):
       return '%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['surname']

