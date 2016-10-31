# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0007_auto_20160425_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyCancer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('organ', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudyClips',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('maximum_size_mm', models.IntegerField(blank=True, verbose_name='Maximum size (mm)', null=True)),
                ('area_square_cm', models.IntegerField(blank=True, verbose_name='Area (cm2)', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudyInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='case',
            name='antiplatelet_anticoagulant',
        ),
        migrations.RemoveField(
            model_name='case',
            name='argon_coagulacion',
        ),
        migrations.RemoveField(
            model_name='case',
            name='resection_yn',
        ),
        migrations.AlterField(
            model_name='case',
            name='bleeding',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'During no clinical impact-autol'), (2, 'During exploration with clinical impact'), (3, '24h'), (4, '24-48h'), (5, '3-7 days'), (6, '>7 days')], verbose_name='Bleeding', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='clips_tratment_group',
            field=models.IntegerField(blank=True, choices=[(1, 'Complete closure with complete mucosal apposition'), (2, 'Complete closure without complete mucosal apposition'), (3, 'Total failed closure'), (4, 'Partial failed closure'), (5, 'Closure not tried')], verbose_name='Clips treatment group', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='endocut',
            field=models.IntegerField(blank=True, choices=[(1, 'Only cut current'), (2, 'Only coagulation current'), (3, 'Endocut/Blended')], verbose_name='Endocut/Blended', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='immediate_bleeding',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes: during exploration with clinical impact'), (2, 'Yes: during exploration without clinical impact')], verbose_name='Immediate bleeding', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='limit_marks',
            field=models.IntegerField(blank=True, choices=[(0, 'No marks'), (1, 'APC marks')], verbose_name='Limit marks', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.IntegerField(blank=True, verbose_name='Active ingredients anticoagulant/antiagregant', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='not_tired_closure_by',
            field=models.IntegerField(blank=True, choices=[(1, 'Big size'), (2, 'Difficult location'), (3, 'Both')], verbose_name='Closure not tried because of', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='pain_requiring_medical_intervention',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Pain requiring medical intervantion', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='pps',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], verbose_name='Post polypectomy syndrome', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='recurrenec_one_year_control',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes: positive biopsy: endoscopic treatment'), (2, 'Yes: visible recurrence: endoscopic treatment'), (3, 'Yes: surgical treatment needed')], verbose_name='Recurrence 1 year control', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='time_of_procedure_in_mins',
            field=models.IntegerField(blank=True, verbose_name='Time of procedure (m)', null=True),
        ),
        migrations.AddField(
            model_name='studyclips',
            name='info',
            field=models.ForeignKey(related_name='info_studyclips', to='clips_app.StudyInfo'),
        ),
        migrations.AddField(
            model_name='studycancer',
            name='info',
            field=models.ForeignKey(related_name='info_studycancer', to='clips_app.StudyInfo'),
        ),
    ]
