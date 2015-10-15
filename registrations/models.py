from django.db import models

MODULECHOICES = ((1, 'Single crystal diffraction'),
                 (2, 'Powder diffraction'))

STATUSCHOICES = ((1, 'participant'),
                 (2, 'lecturer'),
                 (3, 'accompanying person'))

class Registration(models.Model):
    "Stores registration and payment information"
    name = models.CharField(max_length=50, verbose_name="Name")
    surname = models.CharField(max_length=50, verbose_name="Surname")
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField(verbose_name="Date of birth", help_text="Format dd-mm-yyyy")
    affiliation = models.TextField(verbose_name="Affiliation")
    address = models.TextField()
    module = models.IntegerField(choices=MODULECHOICES)
    status = models.IntegerField(choices=STATUSCHOICES, verbose_name="Status at ECS3")



    is_invited = models.BooleanField(default=False, editable=False)
    order = models.PositiveSmallIntegerField(editable=False,null=True,blank=True)


    confirmed = models.NullBooleanField(editable=False)
    paid = models.NullBooleanField(editable=False)
    
    def __unicode__(self):
       return '%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['surname']

