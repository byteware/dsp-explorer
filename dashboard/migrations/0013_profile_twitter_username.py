# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20170713_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='twitter_username',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Twitter Username'),
        ),
    ]
