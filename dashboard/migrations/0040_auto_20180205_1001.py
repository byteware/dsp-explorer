# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-05 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_auto_20180131_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='details',
            field=models.TextField(default='no', verbose_name='Details'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_picture',
            field=models.ImageField(default=0, upload_to='images/company', verbose_name='Company picture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]