# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clips_app', '0002_auto_20160411_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='clips_exp_date',
            field=models.DateField(verbose_name='Expiration date', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='clips_n_lote',
            field=models.IntegerField(verbose_name='Lot number', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='snare_tip_soft_coagulation',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Snare tip soft coagulation', null=True, blank=True),
        ),
    ]
