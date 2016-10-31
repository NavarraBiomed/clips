# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studies_app', '0020_auto_20161031_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.ForeignKey(to='studies_app.Hospital')),
                ('studies', models.ManyToManyField(to='studies_app.Study')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='clips_userprofile')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofilestudies',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='UserProfileStudies'),
        ),
    ]
