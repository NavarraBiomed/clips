# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0003_auto_20160414_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='case',
            name='name',
        ),
        migrations.AlterField(
            model_name='case',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], verbose_name='Age interval', max_length=2, blank=True, null=True),
        ),
    ]
