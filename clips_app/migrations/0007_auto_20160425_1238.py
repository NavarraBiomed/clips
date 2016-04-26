# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0006_auto_20160418_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='inr',
            field=models.FloatField(verbose_name='INR', blank=True, null=True),
        ),
    ]
