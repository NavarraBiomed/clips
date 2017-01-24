# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0016_auto_20161223_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='budding',
            field=models.IntegerField(null=True, choices=[(0, 'No or low grade'), (1, 'High grade')], verbose_name='Budding**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='correct_dx_adenoma_serrated',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Adenoma Serrated*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='correct_dx_invasion',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Correct Dx Invasion*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='degree_differentiation',
            field=models.IntegerField(null=True, choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')], verbose_name='Degree differentiation**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='depth',
            field=models.IntegerField(null=True, choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')], verbose_name='Depth**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(null=True, verbose_name='Depth (Sm invasion: µ)**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='endoscopic_technique',
            field=models.IntegerField(null=True, choices=[(1, 'Patient sent to surgery '), (2, 'EMR'), (3, 'Hybrid EMR'), (4, 'ESD'), (5, 'Full-thickness resection')], verbose_name='Endoscopic technique*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free horizontal margin (>1mm)**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')], verbose_name='Free vertical margins (>1mm)**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='histological_variants',
            field=models.IntegerField(null=True, choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')], verbose_name='Histological variants**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='histology',
            field=models.IntegerField(null=True, choices=[(1, 'Adenoma'), (2, 'HGD to intramucosal carcinoma in adenoma'), (3, 'Superficial submucosal carcinoma in adenoma'), (4, 'Deep submucosal carcinoma in adenoma'), (5, 'Hyperplastic'), (6, 'Sesil Serrated polyp'), (7, 'Traditional Serrated Adenoma'), (8, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (9, 'HGD to intramucosal carcinoma any serrated'), (10, 'Superficial submucosa carc. Any serrated'), (11, 'Deep submucosa carc. Any serrated'), (12, 'Carcinoid')], verbose_name='Histology*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Lymphatic invasion**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='perineural_invasion',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Perineural invasion**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_a',
            field=models.IntegerField(null=True, choices=[(1, 'Adenoma'), (2, 'Serrated')], verbose_name='Prepathologic endoscopic diagnost 1*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='prepathologic_endoscopic_diagnostic_b',
            field=models.IntegerField(null=True, choices=[(1, 'NodisplasiaToSuperficial submucosal carcinoma'), (2, 'Deep submucosal carcinoma')], verbose_name='Prepathologic endoscopic diagnost 2*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='sedation',
            field=models.IntegerField(null=True, choices=[(0, 'Without sedation'), (1, 'By gastroenterologist other than Propofol'), (2, 'By gastroenterologist based on Propofol'), (3, 'By anesthesiologist')], verbose_name='Sedation*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='surgery',
            field=models.IntegerField(null=True, choices=[(0, 'Not needed'), (1, 'Primary for technical reasons'), (2, 'Primary for suspected invasiveness'), (3, 'Due to bleeding (after EMR)'), (4, 'Due to perforation (after EMR)'), (5, 'Histological reasons (after EMR)'), (6, 'Clinical/patient decision (after EMR)')], verbose_name='Surgery*', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='vascular_invasion',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Vascular invasion**', blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='visible_scar',
            field=models.IntegerField(null=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Visible scar*', blank=True),
        ),
    ]
