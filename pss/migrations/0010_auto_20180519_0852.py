# Generated by Django 2.0.5 on 2018-05-19 08:52

import django.core.files.storage
from django.db import migrations, models
import pss.models


class Migration(migrations.Migration):

    dependencies = [
        ('pss', '0009_auto_20180515_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='zip_location',
            field=models.FileField(max_length=500, storage=django.core.files.storage.FileSystemStorage(location='pss/application'), upload_to=pss.models.upload_to_and_rename, verbose_name='Zip Location'),
        ),
    ]
