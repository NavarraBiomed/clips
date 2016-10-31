# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0009_auto_20161021_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancercase',
            name='info',
            field=models.ForeignKey(related_name='cases_cancercase', to='clips_app.StudyInfo'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='info',
            field=models.ForeignKey(related_name='cases_clipscase', to='clips_app.StudyInfo'),
        ),
    ]
