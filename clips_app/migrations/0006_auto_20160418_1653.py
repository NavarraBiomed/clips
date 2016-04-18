# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0005_auto_20160418_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='id_for_hosptital',
            new_name='id_for_hospital',
        ),
    ]
