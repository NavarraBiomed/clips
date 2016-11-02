# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0007_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='studies',
            field=models.ManyToManyField(to='studies_app.Study'),
        ),
    ]
