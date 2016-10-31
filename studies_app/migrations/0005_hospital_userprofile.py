# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studies_app', '0004_auto_20161024_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('hospital', models.ForeignKey(to='studies_app.Hospital')),
                ('studies', models.ManyToManyField(to='studies_app.Study')),
                ('user', models.OneToOneField(related_name='test_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
