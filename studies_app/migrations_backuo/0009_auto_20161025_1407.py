# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0008_auto_20161025_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancercase',
            name='doctor',
            field=models.ForeignKey(null=True, to='studies_app.UserProfile', verbose_name='Doctor', blank=True),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='doctor',
            field=models.ForeignKey(null=True, to='studies_app.UserProfile', verbose_name='Doctor', blank=True),
        ),
    ]
