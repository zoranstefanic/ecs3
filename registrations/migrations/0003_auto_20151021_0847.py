# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20151016_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 21, 8, 47, 25, 349916, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='accepted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='affiliation',
            field=models.CharField(max_length=200, verbose_name=b'Affiliation'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='arrival',
            field=models.DateField(default=b'2016-09-25', verbose_name=b'Date of arrival'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_of_birth',
            field=models.DateField(verbose_name=b'Date of birth'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='departure',
            field=models.DateField(default=b'2016-10-02', verbose_name=b'Date of departure'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='module',
            field=models.IntegerField(choices=[(1, b'Single crystal diffraction'), (2, b'Powder diffraction')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='paid',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
