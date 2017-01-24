# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0018_study_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='tutorial',
            field=models.FileField(verbose_name='Tutorial file', blank=True, null=True, upload_to='tutorials'),
        ),
    ]
