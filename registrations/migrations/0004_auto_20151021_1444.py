# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_auto_20151021_0847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='registration',
            name='abstract',
            field=models.FileField(help_text=b'Only participants need to upload an abstract', null=True, upload_to=b'abstracts', blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.IntegerField(verbose_name=b'Status at ECS3', choices=[(1, b'student'), (2, b'lecturer'), (3, b'accompanying person'), (4, b'organizer')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.IntegerField(default=1, choices=[(1, b'Mr.'), (2, b'Ms.'), (3, b'Dr.'), (4, b'Prof.')]),
        ),
    ]
