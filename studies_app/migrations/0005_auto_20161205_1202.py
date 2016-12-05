# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0004_auto_20161205_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observationalcase',
            old_name='cromoendoscopy',
            new_name='chromoendoscopy',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='demacrated_depressed_area',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='hb',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='ileocecal_valve_involvement',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='inr',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='polyp_retrieval',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='pt',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='technique',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='technique_two',
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='boston_left',
            field=models.IntegerField(verbose_name='Boston left colon', null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='boston_right',
            field=models.IntegerField(verbose_name='Boston right colon', null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='boston_total',
            field=models.IntegerField(verbose_name='Boston', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='boston_transverse',
            field=models.IntegerField(verbose_name='Boston transverse colon', null=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='demarcated_depressed_area',
            field=models.IntegerField(verbose_name='Demarcated depressed area', null=True, choices=[(0, 'No'), (1, 'Yes')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='difficult_locations',
            field=models.IntegerField(verbose_name='Difficult locations', null=True, choices=[(1, 'Ileo-cecal valve'), (2, 'Ileo-cecal valve+ distal ileum'), (3, 'Dentate line'), (4, 'Diverticula'), (5, 'Appendix')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='dye_submucosal_injection',
            field=models.IntegerField(verbose_name='Dye submucosal injection', null=True, choices=[(0, 'No'), (1, 'Indigo carmin'), (3, 'Methylene blue')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='endoscopic_technique',
            field=models.IntegerField(verbose_name='Endoscopic technique', null=True, choices=[(1, 'Patient sent to surgery '), (2, 'EMR'), (3, 'Hybrid EMR'), (4, 'ESD'), (5, 'Full-thickness resection')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='laxative',
            field=models.IntegerField(verbose_name='Laxative', null=True, choices=[(1, '4 litre polyethylene glycol (Bohm, Casenglicol)'), (2, 'Polyethylene gylcol plus ascorbate: 2 litres (Moviprep)'), (3, 'Sodium picosulfate, magnesium citrate (Citrafleet)'), (4, 'Fosfates (Fosfosoda)'), (5, 'Sulfates (Eziclen)')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='laxative_schedule',
            field=models.IntegerField(verbose_name='Laxative schedule', null=True, choices=[(1, 'Day before of colonoscopy'), (2, 'Split dose overnight'), (3, 'Same day of colonoscopy')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='other_coagulopathies',
            field=models.IntegerField(verbose_name='Other coagulopathies', null=True, choices=[(0, 'No'), (1, 'Yes')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='treatment_of_residual_polyp',
            field=models.IntegerField(verbose_name='Treatment of residual polyp', null=True, choices=[(1, 'Not necessary'), (2, 'APC'), (3, 'Snare tip coagulation'), (4, 'Cold avulsion plus coagulation'), (5, 'Hot avulsion'), (6, 'KAR (knife assisted resection)')], blank=True),
        ),
        migrations.AddField(
            model_name='observationalcase',
            name='visible_scar',
            field=models.IntegerField(verbose_name='Visible scar', null=True, choices=[(0, 'No'), (1, 'Yes')], blank=True),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='resection',
            field=models.IntegerField(verbose_name='Resection', null=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(verbose_name='Colonoscopy indication', null=True, choices=[(1, 'Symptoms'), (2, 'CRC screening'), (3, 'Follow up'), (4, 'Referred to resection')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(verbose_name='Difficutly of EMR', null=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='injection',
            field=models.IntegerField(verbose_name='Injection', null=True, choices=[(0, 'No'), (1, 'Saline'), (2, 'Glycerol'), (3, 'Hyaluronic'), (4, 'Hydroxypropyl methylcellulose(Voluven®)'), (5, 'Succinylated gelatin (Gelafundina®)'), (6, 'Others')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='limit_marks',
            field=models.IntegerField(verbose_name='Limit marks', null=True, choices=[(0, 'No'), (1, 'Yes')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='location',
            field=models.IntegerField(verbose_name='Location', null=True, choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic flexure'), (6, 'Ascending'), (7, 'Cecum')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nbi',
            field=models.IntegerField(verbose_name='NBI/FICE', null=True, choices=[(0, 'No'), (1, 'Yes')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nbi_nice',
            field=models.IntegerField(verbose_name='NICE', null=True, choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='nbi_sano',
            field=models.IntegerField(verbose_name='SANO', null=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='platelets',
            field=models.IntegerField(verbose_name='Platelets', null=True, choices=[(0, '>150.000'), (1, '150.000-50.000'), (2, '< 50.000')], blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='resection',
            field=models.IntegerField(verbose_name='Resection', null=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')], blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(verbose_name='Colonoscopy indication', null=True, choices=[(1, 'Symptoms'), (2, 'CRC screening'), (3, 'Follow up'), (4, 'Referred to resection')], blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='resection',
            field=models.IntegerField(verbose_name='Resection', null=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')], blank=True),
        ),
    ]
