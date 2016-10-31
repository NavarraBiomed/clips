# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies_app', '0011_auto_20161026_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typecase',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='typecase',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='typecase',
            name='study',
        ),
        migrations.RemoveField(
            model_name='cancercase',
            name='typecase_ptr',
        ),
        migrations.RemoveField(
            model_name='clipscase',
            name='typecase_ptr',
        ),
        migrations.AddField(
            model_name='cancercase',
            name='doctor',
            field=models.ForeignKey(null=True, blank=True, to='studies_app.UserProfile', verbose_name='Doctor'),
        ),
        migrations.AddField(
            model_name='cancercase',
            name='hospital',
            field=models.ForeignKey(null=True, blank=True, to='studies_app.Hospital', default=None),
        ),
        migrations.AddField(
            model_name='cancercase',
            name='id',
            field=models.AutoField(primary_key=True, default=0, auto_created=True, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cancercase',
            name='study',
            field=models.ForeignKey(related_name='cases_cancercase', to='studies_app.Study', verbose_name='Study', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clipscase',
            name='doctor',
            field=models.ForeignKey(null=True, blank=True, to='studies_app.UserProfile', verbose_name='Doctor'),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='hospital',
            field=models.ForeignKey(null=True, blank=True, to='studies_app.Hospital', default=None),
        ),
        migrations.AddField(
            model_name='clipscase',
            name='id',
            field=models.AutoField(primary_key=True, default=0, auto_created=True, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clipscase',
            name='study',
            field=models.ForeignKey(related_name='cases_clipscase', to='studies_app.Study', verbose_name='Study', default=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TypeCase',
        ),
    ]
