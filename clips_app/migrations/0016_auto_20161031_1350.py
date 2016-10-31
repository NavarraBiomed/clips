# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0015_auto_20161031_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='studies',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='case',
            name='doctor',
            field=models.ForeignKey(blank=True, verbose_name='Doctor', to='studies_app.UserProfile', null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
