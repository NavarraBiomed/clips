# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0013_auto_20161026_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clipscase',
            old_name='clips',
            new_name='treatment_group',
        ),
        migrations.AddField(
            model_name='cancercase',
            name='treatment_group',
            field=models.IntegerField(verbose_name='Clips', blank=True, choices=[(0, 'Control group'), (1, 'Treatment group')], null=True),
        ),
    ]
