# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0019_auto_20161031_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilestudies',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, to='studies_app.Hospital'),
        ),
    ]
