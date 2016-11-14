# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipscase',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], null=True, blank=True, verbose_name='Age interval'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='nombre_p_activo_antiagreg_anticoag',
            field=models.CharField(max_length=128, null=True, blank=True, verbose_name='Active ingredients anticoagulant/antiagregant'),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, blank=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], null=True, blank=True, verbose_name='Age interval'),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, blank=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '< 60'), (2, '60-74'), (3, '>= 75')], null=True, blank=True, verbose_name='Age interval'),
        ),
        migrations.AlterField(
            model_name='obsinternationalcase',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, blank=True, verbose_name='Sex'),
        ),
    ]
