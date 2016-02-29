# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0002_auto_20160203_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='hospital',
            field=models.ForeignKey(default=None, to='clips_app.Hospital'),
        ),
    ]
