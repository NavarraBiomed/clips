# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0022_auto_20161031_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilestudies',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='userprofilestudies',
            name='studies',
        ),
        migrations.RemoveField(
            model_name='userprofilestudies',
            name='user',
        ),
        migrations.AlterField(
            model_name='cancercase',
            name='doctor',
            field=models.ForeignKey(blank=True, verbose_name='Doctor', null=True, to='studies_app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='doctor',
            field=models.ForeignKey(blank=True, verbose_name='Doctor', null=True, to='studies_app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='doctor',
            field=models.ForeignKey(blank=True, verbose_name='Doctor', null=True, to='studies_app.UserProfile'),
        ),
        migrations.DeleteModel(
            name='UserProfileStudies',
        ),
    ]
