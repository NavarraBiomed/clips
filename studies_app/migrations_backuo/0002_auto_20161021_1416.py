# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='study',
            options={'verbose_name_plural': 'Studies'},
        ),
    ]
