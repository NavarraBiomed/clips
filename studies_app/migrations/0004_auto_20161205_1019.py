# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0003_auto_20161114_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='observationalcase',
            name='case_number',
            field=models.IntegerField(null=True, verbose_name='Number of case for patient', blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='endoscopist',
            field=models.CharField(blank=True, null=True, verbose_name='Endoscopist', max_length=128),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='id_number',
            field=models.IntegerField(null=True, verbose_name='ID Number', blank=True),
        ),
    ]
