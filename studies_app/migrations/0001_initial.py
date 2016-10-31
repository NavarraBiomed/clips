# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CancerCase',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('organ', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClipsCase',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('maximum_size_mm', models.IntegerField(blank=True, null=True, verbose_name='Maximum size (mm)')),
                ('area_square_cm', models.IntegerField(blank=True, null=True, verbose_name='Area (cm2)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='clipscase',
            name='info',
            field=models.ForeignKey(to='studies_app.Study', related_name='cases_clipscase'),
        ),
        migrations.AddField(
            model_name='cancercase',
            name='info',
            field=models.ForeignKey(to='studies_app.Study', related_name='cases_cancercase'),
        ),
    ]
