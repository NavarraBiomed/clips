# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0004_auto_20160416_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='id_for_doctor',
            field=models.IntegerField(null=True, blank=True, verbose_name='Id for doctor'),
        ),
        migrations.AddField(
            model_name='case',
            name='id_for_hosptital',
            field=models.IntegerField(null=True, blank=True, verbose_name='Id for hospital'),
        ),
    ]
