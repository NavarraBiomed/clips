# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0015_auto_20161223_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='age',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Age*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='boston_left',
            field=models.IntegerField(blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston left colon*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='boston_right',
            field=models.IntegerField(blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston right colon*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='boston_transverse',
            field=models.IntegerField(blank=True, choices=[(0, 'Solid'), (1, 'Semisolid'), (2, 'Liquid'), (3, 'Excelent')], verbose_name='Boston transverse colon*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='case_number',
            field=models.IntegerField(blank=True, verbose_name='Case number*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='chicken_skin_mucosa_around',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chicken skin mucosa around*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='chromoendoscopy',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Chromoendoscopy*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='colonoscopy_indication',
            field=models.IntegerField(blank=True, choices=[(1, 'Symptoms'), (2, 'CRC screening'), (3, 'Follow up'), (4, 'Referred to resection')], verbose_name='Colonoscopy indication*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='country',
            field=models.IntegerField(blank=True, choices=[(1, 'Spain'), (2, 'Japan'), (3, 'UK'), (4, 'USA'), (5, 'China')], verbose_name='Country*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='date',
            field=models.DateField(blank=True, verbose_name='Date*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='demarcated_depressed_area',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Demarcated depressed area*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='difficult_locations',
            field=models.IntegerField(blank=True, choices=[(1, 'Ileo-cecal valve'), (2, 'Ileo-cecal valve+ distal ileum'), (3, 'Dentate line'), (4, 'Diverticula'), (5, 'Appendix')], verbose_name='Difficult locations*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='difficulty_of_emr',
            field=models.IntegerField(blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Difficult')], verbose_name='Technique of EMR', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='endoscopemodel',
            field=models.CharField(blank=True, max_length=50, verbose_name='Endoscope model*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='endoscopist',
            field=models.CharField(blank=True, max_length=128, verbose_name='Endoscopist*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='fold_convergency',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Fold convergency*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='high_definition',
            field=models.IntegerField(blank=True, choices=[(1, 'Conventional endoscope'), (2, 'High definition'), (3, 'Optic magnification')], verbose_name='High definition*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='id_number',
            field=models.IntegerField(blank=True, verbose_name='ID*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='kudo',
            field=models.IntegerField(blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIS'), (4, 'IIIL'), (5, 'IV'), (6, 'V-I'), (7, 'V-N')], verbose_name='Kudo*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='large_nodule_one_cm',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Large nodule 1cm*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='laxative',
            field=models.IntegerField(blank=True, choices=[(1, '4 litre polyethylene glycol (Bohm, Casenglicol...)'), (2, 'Polyethylene gylcol plus ascorbate: 2 litres (Moviprep...)'), (3, 'Sodium picosulfate, magnesium citrate (Citrafleet...)'), (4, 'Fosfates (Fosfosoda...)'), (5, 'Sulfates (Eziclen...)')], verbose_name='Laxative*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='laxative_schedule',
            field=models.IntegerField(blank=True, choices=[(1, 'Day before of colonoscopy'), (2, 'Split dose overnight'), (3, 'Same day of colonoscopy')], verbose_name='Laxative schedule*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='location',
            field=models.IntegerField(blank=True, choices=[(1, 'Rectum'), (2, 'Left colon'), (3, 'Splenic flexure'), (4, 'Transverse'), (5, 'Hepatic flexure'), (6, 'Ascending'), (7, 'Cecum')], verbose_name='Location*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='lst_morphology',
            field=models.IntegerField(blank=True, choices=[(1, 'Granular homogeneous'), (2, 'Focal nodular mixed type'), (3, 'Whole nodular mixed type'), (4, 'Flat elevated'), (5, 'Psudodepressed')], verbose_name='LST Morphology*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='lst_yn',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='LST yn*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='maximum_size_mm',
            field=models.IntegerField(blank=True, verbose_name='Maximum size (mm)*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='nbi',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='NBI/FICE*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='nbi_nice',
            field=models.IntegerField(blank=True, choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], verbose_name='NICE*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='nbi_sano',
            field=models.IntegerField(blank=True, choices=[(1, 'I'), (2, 'II'), (3, 'IIIA'), (4, 'IIIB')], verbose_name='SANO*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='non_lifting_sign',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Non lifting sign*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='paris_calif',
            field=models.IntegerField(blank=True, choices=[(1, '0Is'), (2, '0IIa'), (3, '0IIa+0Is'), (4, '0Is+0IIa'), (5, '0IIb'), (6, '0IIc'), (7, '0IIa+0IIc'), (8, '0IIb+0IIc'), (9, '0IIb+0IIa')], verbose_name='Paris Clasif.*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='previous_attempt',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous attempt*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='previous_biopsy',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Previous biopsy*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='resection',
            field=models.IntegerField(blank=True, choices=[(1, 'Piecemeal complete'), (2, 'Piecemeal incomplete'), (3, 'En bloc R0'), (4, 'En bloc incomplete')], verbose_name='Resection*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='sclerous_wall_change',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Sclerous wall change*', null=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], verbose_name='Sex*', null=True),
        ),
    ]
