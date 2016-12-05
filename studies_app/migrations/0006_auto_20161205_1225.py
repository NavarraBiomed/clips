# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0005_auto_20161205_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observationalcase',
            name='clips_control_group',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='clips_exp_date',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='clips_n_lote',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='clips_tratment_group',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='cs_coagulation_mode',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='cs_coagulation_watts',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='cs_cut_mode',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='cs_cut_watts',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='histol_simplified',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='not_tired_closure_by',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='surgery_by_complication',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='surgery_from_endoscopy',
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='clipping',
            field=models.IntegerField(blank=True, null=True, verbose_name='Clipping', choices=[(0, 'No'), (1, 'Punctual (VISIBLE\xa0VESSEL)'), (2, 'Partially clipped'), (3, 'Complete clip closure')]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='number_of_sessions',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of endoscopic sessions needed', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='surgery',
            field=models.IntegerField(blank=True, null=True, verbose_name='Surgery', choices=[(0, 'No needed'), (1, 'Primary for technical reasons'), (2, 'Primary for suspected invasiveness'), (3, 'Due to bleeding'), (4, 'Due to perforation'), (5, 'Histological reasons'), (6, 'Clinical/patient decision')]),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='bleeding_treatment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bleeding treatment', choices=[(0, 'No'), (1, 'Injection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods'), (6, 'Snare tip coagulation')]),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by complication (days)'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by technique (days)'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bleeding treatment', choices=[(0, 'No'), (1, 'Injection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods'), (6, 'Snare tip coagulation')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='budding',
            field=models.IntegerField(blank=True, null=True, verbose_name='Budding', choices=[(0, 'No or low grade'), (1, 'High grade')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='histology',
            field=models.IntegerField(blank=True, null=True, verbose_name='Histology', choices=[(1, 'Adenoma'), (2, 'HGD to intramucosal carcinoma in adenoma'), (3, 'Superficial submucosal carcinoma in adenoma'), (4, 'Deep submucosal carcinoma in adenoma'), (5, 'Hyperplastic'), (6, 'Sesil Serrated polyp'), (7, 'Traditional Serrated Adenoma'), (8, 'Polyp Serrated Mixed or serrated polyp with dysplasia'), (9, 'HGD to intramucosal carcinoma any serrated'), (10, 'Superficial submucosa carc. Any serrated'), (11, 'Deep submucosa carc. Any serrated'), (12, 'Carcinoid')]),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='hospital_stay_by_complication',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by complication (days)'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='hospital_stay_by_technique',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hospital stay by technique (days)'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='successful_treatment',
            field=models.IntegerField(blank=True, null=True, verbose_name=' Successful treatment', choices=[(0, 'No (surgery)'), (1, 'Yes (endoscopic treatment)')]),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='bleeding_treatment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bleeding treatment', choices=[(0, 'No'), (1, 'Injection'), (2, 'Clipping'), (3, 'ArgonPC'), (4, 'Coagulation forceps'), (5, '2 methods'), (6, 'Snare tip coagulation')]),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='budding',
            field=models.IntegerField(blank=True, null=True, verbose_name='Budding', choices=[(0, 'No or low grade'), (1, 'High grade')]),
        ),
    ]
