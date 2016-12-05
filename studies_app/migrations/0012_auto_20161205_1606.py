# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0011_auto_20161205_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
