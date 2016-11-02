# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0024_auto_20161031_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationalinternationalCase',
            fields=[
                ('observationalcase_ptr', models.OneToOneField(to='studies_app.ObservationalCase', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('studies_app.observationalcase',),
        ),
        migrations.AlterField(
            model_name='study',
            name='study_type',
            field=models.CharField(max_length=64, choices=[('clips', 'Clips Study'), ('cancer', 'Cancer Study'), ('observational', 'Observational Study'), ('observationalinternational', 'International Observational Study')], verbose_name='Study type'),
        ),
    ]
