# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0005_hospital_userprofile'),
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
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
