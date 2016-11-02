# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0021_auto_20161031_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hospital',
            field=models.ForeignKey(to='studies_app.Hospital', null=True),
        ),
    ]
