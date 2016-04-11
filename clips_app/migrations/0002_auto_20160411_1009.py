# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='doctor',
            field=models.ForeignKey(blank=True, verbose_name='Doctor', to='clips_app.UserProfile', null=True),
        ),
    ]
