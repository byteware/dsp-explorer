# Generated by Django 2.0.5 on 2018-05-21 07:47

import dashboard.models
from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0061_auto_20180519_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='place',
            field=django_mysql.models.JSONField(default=dashboard.models.default_place, null=True),
        ),
    ]
