# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0012_auto_20161025_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='studies',
            field=models.ManyToManyField(to='clips_app.Study', related_name='clips_study'),
        ),
    ]
