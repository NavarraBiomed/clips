# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0002_auto_20161114_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(verbose_name='Active ingredients anticoagulant/antiagregant', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(verbose_name='Active ingredients anticoagulant/antiagregant', max_length=128, null=True, blank=True),
        ),
    ]
