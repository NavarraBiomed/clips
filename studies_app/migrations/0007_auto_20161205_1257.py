# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0006_auto_20161205_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observationalcase',
            old_name='boston_total',
            new_name='boston',
        ),
    ]
