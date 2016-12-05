# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0012_auto_20161205_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True),
        ),
    ]
