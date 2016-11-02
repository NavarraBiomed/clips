# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0012_auto_20161026_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancercase',
            name='id_for_doctor',
            field=models.IntegerField(verbose_name='Id for doctor', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cancercase',
            name='id_for_hospital',
            field=models.IntegerField(verbose_name='Id for hospital', null=True, blank=True),
        ),
    ]
