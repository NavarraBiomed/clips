# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0008_auto_20161021_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancerCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('organ', models.CharField(max_length=16)),
                ('info', models.ForeignKey(related_name='info_cancercase', to='clips_app.StudyInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClipsCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('maximum_size_mm', models.IntegerField(verbose_name='Maximum size (mm)', blank=True, null=True)),
                ('area_square_cm', models.IntegerField(verbose_name='Area (cm2)', blank=True, null=True)),
                ('info', models.ForeignKey(related_name='info_clipscase', to='clips_app.StudyInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='studycancer',
            name='info',
        ),
        migrations.RemoveField(
            model_name='studyclips',
            name='info',
        ),
        migrations.DeleteModel(
            name='StudyCancer',
        ),
        migrations.DeleteModel(
            name='StudyClips',
        ),
    ]
