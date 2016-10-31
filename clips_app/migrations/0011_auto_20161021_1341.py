# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0010_auto_20161021_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancercase',
            name='info',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='info',
        ),
        migrations.DeleteModel(
            name='CancerCase',
        ),
        migrations.DeleteModel(
            name='ClipsCase',
        ),
        migrations.DeleteModel(
            name='StudyInfo',
        ),
    ]
