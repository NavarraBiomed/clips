# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0014_auto_20161223_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationalcase',
            name='last_date_endoscopic_follow_up',
            field=models.DateField(null=True, blank=True, verbose_name='Last date endoscopic follow up*'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='recurrence_three_six_months_control',
            field=models.IntegerField(null=True, verbose_name='Recurrence 3-6 months control*', blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='recurrenec_one_year_control',
            field=models.IntegerField(null=True, verbose_name='Recurrence 1 year control*', blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='sedation',
            field=models.IntegerField(null=True, verbose_name='Sedation*', blank=True, choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='successful_treatment',
            field=models.IntegerField(null=True, verbose_name=' Successful treatment*', blank=True, choices=[(0, 'No (surgery)'), (1, 'Yes (endoscopic treatment)')]),
        ),
    ]
