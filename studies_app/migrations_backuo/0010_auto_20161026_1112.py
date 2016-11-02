# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0009_auto_20161025_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('doctor', models.ForeignKey(to='studies_app.UserProfile', blank=True, null=True, verbose_name='Doctor')),
                ('hospital', models.ForeignKey(to='studies_app.Hospital', blank=True, null=True, default=None)),
                ('study', models.ForeignKey(to='studies_app.Study', related_name='cases_typecase', verbose_name='Study')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='cancercase',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='cancercase',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cancercase',
            name='study',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='area_square_cm',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='id',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='maximum_size_mm',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='study',
        ),
        migrations.AddField(
            model_name='cancercase',
            name='typecase_ptr',
            field=models.OneToOneField(to='studies_app.TypeCase', primary_key=True, serialize=False, parent_link=True, auto_created=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clipscase',
            name='typecase_ptr',
            field=models.OneToOneField(to='studies_app.TypeCase', primary_key=True, serialize=False, parent_link=True, auto_created=True, default=None),
            preserve_default=False,
        ),
    ]
