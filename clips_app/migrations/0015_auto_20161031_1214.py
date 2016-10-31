# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clips_app', '0014_auto_20161031_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.ForeignKey(to='clips_app.Hospital')),
                ('studies', models.ManyToManyField(to='clips_app.Study')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='clips_userprofile')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofileclips',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='userprofileclips',
            name='studies',
        ),
        migrations.RemoveField(
            model_name='userprofileclips',
            name='user',
        ),
        migrations.AlterField(
            model_name='case',
            name='doctor',
            field=models.ForeignKey(verbose_name='Doctor', to='clips_app.UserProfile', blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserProfileClips',
        ),
    ]
