# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20151021_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='full_board',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='lunch_box',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='module',
        ),
        migrations.AlterField(
            model_name='registration',
            name='arrival',
            field=models.DateField(default=b'2017-04-22', verbose_name=b'Date of arrival'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='departure',
            field=models.DateField(default=b'2017-04-26', verbose_name=b'Date of departure'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.IntegerField(verbose_name=b'Status at HTCC2017', choices=[(1, b'student'), (2, b'lecturer'), (3, b'accompanying person'), (4, b'organizer'), (5, b'sponsor representative')]),
        ),
    ]
