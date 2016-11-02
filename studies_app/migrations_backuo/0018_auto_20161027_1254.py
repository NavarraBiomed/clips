# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0017_auto_20161027_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='observationalcase',
            name='budding',
            field=models.IntegerField(blank=True, verbose_name='Budding', null=True, choices=[(0, 'No'), (1, 'High grade')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(blank=True, verbose_name='Colonoscopy indication', null=True, choices=[(1, 'Anemia/iron deficiency'), (2, 'CRC suspected'), (3, 'CRC screening program'), (4, 'Postpolypectomy surveillance'), (5, 'Relatives with CRC or polyposis'), (6, 'Polyposis'), (7, 'Other')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='country',
            field=models.IntegerField(blank=True, verbose_name='Country', null=True, choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='degree_differentiation',
            field=models.IntegerField(blank=True, verbose_name='Degree differentiation', null=True, choices=[(1, 'Well'), (2, 'Moderate'), (3, 'Poorly')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='depth',
            field=models.IntegerField(blank=True, verbose_name='Depth', null=True, choices=[(1, 'Mucosa'), (2, 'SM1'), (3, 'SM2'), (4, 'SM3'), (5, 'MP or deeper')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='depth_sm_invasion',
            field=models.FloatField(blank=True, verbose_name='Depth (Sm invasion: µ)', null=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='free_horizontal_margins',
            field=models.IntegerField(blank=True, verbose_name='Free horizontal margin (>1mm)', null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='free_vertical_margins',
            field=models.IntegerField(blank=True, verbose_name='Free vertical margins (>1mm)', null=True, choices=[(1, 'Nonassessable'), (2, 'Free'), (3, 'Affected')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='histological_variants',
            field=models.IntegerField(blank=True, verbose_name='Histological variants', null=True, choices=[(1, 'Adenocarcinoma'), (2, 'Mucinous'), (3, 'Medullary'), (4, 'Signet ring')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='lymphatic_invasion',
            field=models.IntegerField(blank=True, verbose_name='Lymphatic invasion', null=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='perineural_invasion',
            field=models.IntegerField(blank=True, verbose_name='Perineural invasion', null=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='vascular_invasion',
            field=models.IntegerField(blank=True, verbose_name='Vascular invasion', null=True, choices=[(0, 'No'), (1, 'Yes')]),
        ),
    ]
