# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clips_app', '0013_auto_20161025_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileClips',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('hospital', models.ForeignKey(to='clips_app.Hospital')),
                ('studies', models.ManyToManyField(to='clips_app.Study')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='clips_userprofile')),
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
            model_name='case',
            name='doctor',
            field=models.ForeignKey(null=True, verbose_name='Doctor', to='clips_app.UserProfileClips', blank=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
