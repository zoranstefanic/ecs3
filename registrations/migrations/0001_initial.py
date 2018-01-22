# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.IntegerField(default=1, choices=[(1, b'Mr.'), (2, b'Ms.'), (3, b'Dr.'), (4, b'Prof.')])),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('surname', models.CharField(max_length=50, verbose_name=b'Surname')),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('date_of_birth', models.DateField(verbose_name=b'Date of birth')),
                ('affiliation', models.CharField(max_length=200, verbose_name=b'Affiliation')),
                ('address', models.CharField(max_length=100)),
                ('status', models.IntegerField(verbose_name=b'Status at HTCC2018', choices=[(1, b'student'), (2, b'lecturer'), (3, b'accompanying person'), (4, b'organizer'), (5, b'sponsor representative')])),
                ('bursary', models.BooleanField(default=False, help_text=b'I would like to apply for bursary')),
                ('cv', models.FileField(help_text=b'Upload your CV.', upload_to=b'bursaries', null=True, verbose_name=b'Curriculum vitae', blank=True)),
                ('mot_letter', models.FileField(help_text=b'Upload your motivation letter.', upload_to=b'bursaries', null=True, verbose_name=b'Motivation letter', blank=True)),
                ('rec_letter', models.FileField(help_text=b'Upload your recommendation letter.', upload_to=b'bursaries', null=True, verbose_name=b'Recommandation letter', blank=True)),
                ('hotel_category', models.IntegerField(default=1, choices=[(1, b'3***'), (2, b'4****')])),
                ('room_choice', models.IntegerField(default=1, choices=[(1, b'shared double room'), (2, b'double room single use')])),
                ('room_preference', models.CharField(max_length=50, null=True, verbose_name=b'I would like to share the room with', blank=True)),
                ('arrival', models.DateField(default=b'2018-09-23', verbose_name=b'Date of arrival')),
                ('departure', models.DateField(default=b'2018-09-27', verbose_name=b'Date of departure')),
                ('accepted', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False, editable=False)),
                ('code', models.PositiveSmallIntegerField(default=registrations.models.generate_code, editable=False)),
                ('topic1_expertise', models.IntegerField(default=1, help_text=b'How would your rate your expertise in Hot topic 1: Extreme conditions', choices=[(1, b'biginner'), (2, b'intermediate'), (3, b'advanced')])),
                ('topic2_expertise', models.IntegerField(default=1, help_text=b'How would your rate your expertise in Hot topic 2: Total scattering and PDF analysis of complex materials', choices=[(1, b'biginner'), (2, b'intermediate'), (3, b'advanced')])),
                ('topic3_expertise', models.IntegerField(default=1, help_text=b'How would your rate your expertise in Hot topic 3: Dynamical crystallography', choices=[(1, b'biginner'), (2, b'intermediate'), (3, b'advanced')])),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
