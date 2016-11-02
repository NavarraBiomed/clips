# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0016_auto_20161027_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancercase',
            name='group',
            field=models.IntegerField(verbose_name='Group', choices=[(0, 'Control group'), (1, 'Treatment group')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='group',
            field=models.IntegerField(verbose_name='Group', choices=[(0, 'Control group'), (1, 'Treatment group')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='group',
            field=models.IntegerField(verbose_name='Group', choices=[(0, 'Control group'), (1, 'Treatment group')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
