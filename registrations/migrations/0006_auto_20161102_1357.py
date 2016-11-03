# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0005_auto_20161102_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='bursary',
            field=models.BooleanField(default=False, help_text=b'I would like to apply for bursary'),
        ),
        migrations.AddField(
            model_name='registration',
            name='cv',
            field=models.FileField(help_text=b'Upload your CV.', null=True, upload_to=b'bursaries', blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='mot_letter',
            field=models.FileField(help_text=b'Upload your motivation letter.', null=True, upload_to=b'bursaries', blank=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='rec_letter',
            field=models.FileField(help_text=b'Upload your recommendation letter.', null=True, upload_to=b'bursaries', blank=True),
        ),
    ]
