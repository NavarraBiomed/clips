# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studies_app', '0018_auto_20161027_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileStudies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.ForeignKey(to='studies_app.Hospital')),
                ('studies', models.ManyToManyField(to='studies_app.Study')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='studies',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='cancercase',
            name='doctor',
            field=models.ForeignKey(verbose_name='Doctor', to='studies_app.UserProfileStudies', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clipscase',
            name='doctor',
            field=models.ForeignKey(verbose_name='Doctor', to='studies_app.UserProfileStudies', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='observationalcase',
            name='doctor',
            field=models.ForeignKey(verbose_name='Doctor', to='studies_app.UserProfileStudies', blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
