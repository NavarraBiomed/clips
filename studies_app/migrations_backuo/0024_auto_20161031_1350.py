# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0023_auto_20161031_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancercase',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='observationalcase',
            name='hospital',
        ),
    ]
