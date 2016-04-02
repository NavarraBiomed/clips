# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0003_study_hospital'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='study',
            options={'verbose_name_plural': 'Studies'},
        ),
        migrations.RemoveField(
            model_name='study',
            name='tramos_edad',
        ),
        migrations.AddField(
            model_name='study',
            name='age_interval',
            field=models.CharField(max_length=2, choices=[(1, '<= 60'), (2, '67-74'), (3, '>= 75')], verbose_name='Age interval', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='study',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Age'),
        ),
    ]
