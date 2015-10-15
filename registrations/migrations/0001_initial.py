# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('surname', models.CharField(max_length=50, verbose_name=b'Surname')),
                ('email', models.EmailField(max_length=50)),
                ('affiliation', models.TextField(verbose_name=b'Affiliation')),
                ('address', models.TextField()),
                ('confirmed', models.NullBooleanField(editable=False)),
                ('paid', models.NullBooleanField(editable=False)),
                ('date_of_birth', models.DateField(verbose_name=b'Date of birth')),
                ('module', models.IntegerField(choices=[(1, b'Single crystal diffraction'), (2, b'Powder diffraction')])),
                ('status', models.IntegerField(verbose_name=b'Status at ECS3', choices=[(1, b'participant'), (2, b'lecturer'), (3, b'accompanying person')])),
                ('is_invited', models.BooleanField(default=False, editable=False)),
                ('order', models.PositiveSmallIntegerField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
    ]
