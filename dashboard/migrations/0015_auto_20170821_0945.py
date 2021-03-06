# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20170718_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(to='dashboard.Tag'),
        ),
    ]
