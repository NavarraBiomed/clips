# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0003_study_study_type'),
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
        migrations.AddField(
            model_name='cancercase',
            name='study',
            field=models.ForeignKey(default=1, verbose_name='Study', to='studies_app.Study', related_name='cases_cancercase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clipscase',
            name='study',
            field=models.ForeignKey(default=None, verbose_name='Study', to='studies_app.Study', related_name='cases_clipscase'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='study',
            name='study_type',
            field=models.CharField(verbose_name='Study type', choices=[('clips', 'Clips Study'), ('cancer', 'Cancer Study')], max_length=64),
        ),
    ]
