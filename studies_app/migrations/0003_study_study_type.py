# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0002_auto_20161021_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='study_type',
            field=models.CharField(choices=[('Clips', 'Clips Study'), ('Cancer', 'Cancer Study')], verbose_name='Study type', default='Clips', max_length=64),
            preserve_default=False,
        ),
    ]
