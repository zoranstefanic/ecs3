# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='confirmed',
            new_name='accepted',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_invited',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='order',
        ),
        migrations.AddField(
            model_name='registration',
            name='abstract',
            field=models.FileField(help_text=b'Only participants need to upload an abstract', null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='arrival',
            field=models.DateField(default=b'2016-09-25', help_text=b'Format dd-mm-yyyy', verbose_name=b'Date of arrival'),
        ),
        migrations.AddField(
            model_name='registration',
            name='code',
            field=models.PositiveSmallIntegerField(default=registrations.models.generate_code, editable=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='departure',
            field=models.DateField(default=b'2016-10-02', help_text=b'Format dd-mm-yyyy', verbose_name=b'Date of departure'),
        ),
        migrations.AddField(
            model_name='registration',
            name='full_board',
            field=models.BooleanField(default=False, help_text=b''),
        ),
        migrations.AddField(
            model_name='registration',
            name='hotel_category',
            field=models.IntegerField(default=1, choices=[(1, b'3***'), (2, b'4****')]),
        ),
        migrations.AddField(
            model_name='registration',
            name='lunch_box',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='room_choice',
            field=models.IntegerField(default=1, choices=[(1, b'shared double room'), (2, b'double room single use')]),
        ),
        migrations.AddField(
            model_name='registration',
            name='room_preference',
            field=models.CharField(max_length=50, null=True, verbose_name=b'I would like to share the room with', blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='title',
            field=models.IntegerField(default=1, choices=[(1, b'Mr.'), (2, b'Ms.'), (3, b'Dr.')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_of_birth',
            field=models.DateField(help_text=b'Format dd-mm-yyyy', verbose_name=b'Date of birth'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='module',
            field=models.IntegerField(default=1, choices=[(1, b'Single crystal diffraction'), (2, b'Powder diffraction')]),
        ),
    ]
