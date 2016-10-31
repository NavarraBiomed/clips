# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0014_auto_20161026_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancercase',
            old_name='treatment_group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='clipscase',
            old_name='treatment_group',
            new_name='group',
        ),
    ]
